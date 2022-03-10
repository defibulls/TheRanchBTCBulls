// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*    
🅣🅗🅔🅡🅐🅝🅒🅗_🅑🅤🅛🅛🅢_➋⓿➋➋
*/


// Confirm royalties are being paid out. 
// Confirm the royalies wallet doesn't have to pay royalties on anything that wallet purchases. 
// DECIMAL variable to help


import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "./TheRanchBullsMint.sol";


contract TheRanchBullsAirDrop is VRFConsumerBase, Ownable {

    AggregatorV3Interface public priceFeed;
    mapping(address => uint256) public addressToAmountFunded;


    address public TheRanchBullsMintAddress;
    address public dev1;
    address public dev2;
    uint256 public dev1_percent = 14;
    uint256 public dev2_percent = 6;
    address public rewardTokenContract;
    uint public rewardDecimals = 18;

    uint public giveawayId;

    event centennial_Air_Drop(
        uint indexed giveawayId,
        uint256 indexed payout_cut,
        uint256[] winners   
    );


    bytes32 public keyhash;
    uint256 public randomResult;
    event RequestedRandomness(bytes32 requestId);

    enum AWARD_STATE {
        OPEN,
        CLOSED,
        PAY_AUTHORIZED
    }
    AWARD_STATE public award_state;
    uint256 public fee;

    constructor(
        address _dev1,
        address _dev2,
        address _vrfCoordinator,
        address _link,
        uint256 _fee,
        bytes32 _keyhash
    ) public
        VRFConsumerBase(_vrfCoordinator, _link) {
        dev1 = _dev1;
        dev2 = _dev2;
        award_state = AWARD_STATE.CLOSED;
        fee = _fee;
        keyhash = _keyhash;    
    }

    // CHAINLINK
    /** 
     * Requests randomness from Chainlink
     */
    function getRandomNumber() private returns (bytes32 requestId) {
        require(LINK.balanceOf(address(this)) >= fee, "Not enough LINK - fill contract with more");
        bytes32 requestId = requestRandomness(keyhash, fee);
        emit RequestedRandomness(requestId);
        return requestId;
    }


    /**
     * Callback function used by VRF Coordinator
     */
    function fulfillRandomness(bytes32 requestId, uint256 randomness) internal override {
        randomResult = randomness;
    }



    /**
     * Expand the single random number from the VRF into more (n) 
    */
    function expand(uint256 randomValue, uint256 n, uint256 _tokenSupply) private returns (uint256[] memory expandedValues) {
        // get the tokenBalance from the minting contract
        // uint256 tokenSupply = getMintTotalSupply();

        require(n <= _tokenSupply, "Looking for too many results, this will infinitely loop");
        expandedValues = new uint256[](n);
        uint found_num;
        uint i = 0;
        while (found_num < n) {
            uint256 num = (uint256(keccak256(abi.encode(randomValue, i))) % _tokenSupply);
            if (num != 0 && num <= _tokenSupply && exists(expandedValues,num) == false) {
                expandedValues[found_num] = num;
                found_num++;
            }
            i++;
        }
        require(expandedValues.length == 100, "We didn't find 100 winners during the expansion");
        // weeklyWinners = expandedValues;
        award_state = AWARD_STATE.PAY_AUTHORIZED;
        return expandedValues;
    }

    /**
     * Assist the expand function to limit the same number twice 
    */
    function exists (uint256[] memory arrayToCheck, uint numberToCheck) private returns (bool) {
        for (uint i = 0; i < arrayToCheck.length; i++) {
            if (arrayToCheck[i] == numberToCheck) {
                return true;
            }
        }
        return false;
    }


  

    // REWARDING of the 100 Bulls after paying out the DEV team
    function centennialAirDrop() public onlyOwner {
        require(award_state == AWARD_STATE.OPEN, "The award state is currently closed");
        require(checkTokenBalance(rewardTokenContract)>= 100 * 10 ** rewardDecimals, "Not Enough Funds to Warrant calling the function to award the Bulls");
        require(award_state == AWARD_STATE.OPEN, "ERROR: The Award function is not open.");
        require(dev1_percent + dev2_percent <= 20, "Dev1 Percent + Dev2 Percent must be lower than 20%");
        // getMintTotalSupply();
    
        // require(getMintTotalSupply() >= 100);

        IERC20 tokenContract = IERC20(rewardTokenContract);

        uint256 _balance = checkTokenBalance(rewardTokenContract);
        tokenContract.transfer(dev1, _balance * dev1_percent / 100);
        tokenContract.transfer(dev2, _balance * dev2_percent / 100);

        _balance = checkTokenBalance(rewardTokenContract);
        uint256 centennial_cut = _balance / 100;

        getRandomNumber();
        uint256 _tokenSupply = getMintTotalSupply();
        uint256[] memory weeklyWinners = expand(randomResult,100, _tokenSupply); 

        require(award_state == AWARD_STATE.PAY_AUTHORIZED);
        
        for (uint256 i = 0; i < weeklyWinners.length; i++) {
            uint winning_index = weeklyWinners[i];
            address luckyBullOwner = getNFTOwnerOf(winning_index);
            tokenContract.transfer(luckyBullOwner, centennial_cut);
        }

        emit centennial_Air_Drop(giveawayId, centennial_cut, weeklyWinners);

        giveawayId++;
        award_state = AWARD_STATE.CLOSED;

    }





    //INFO RETURN


    // Minting contract info
    function setTheRanchBullsMintAddress(address _mintAddress) external {
        TheRanchBullsMintAddress = _mintAddress;
    }

    function getMintTotalSupply() private view returns (uint256) {
        TheRanchBullsMint TRBM = TheRanchBullsMint(TheRanchBullsMintAddress);
        return TRBM.totalSupply();

    }

    function getNFTOwnerOf(uint _index) private view returns (address) {
        TheRanchBullsMint TRBM = TheRanchBullsMint(TheRanchBullsMintAddress);
        return TRBM.ownerOf(_index);
    }

    function verifyNFTOwnerOf(uint _index) public view onlyOwner returns (address) {
        TheRanchBullsMint TRBM = TheRanchBullsMint(TheRanchBullsMintAddress);
        return TRBM.ownerOf(_index);
    }

    function getLinkBalance() public view returns (uint256){
        uint256 _balance = LINK.balanceOf(address(this));
        return _balance;
    }

    function getBalance() public view returns (uint256){
        uint256 _balance = address(this).balance;
        return _balance;
    }

    function getRandomResult() public view returns (uint256){
        return randomResult;
    }

    function checkTokenBalance(address token) public view returns(uint) {
        IERC20 token = IERC20(token);
        return token.balanceOf(address(this));
    }


    // Contract Funding / Withdrawing / Transferring
    function fund() public payable {
        addressToAmountFunded[msg.sender] += msg.value;
    }

    function withdraw(uint256 _amount) external onlyOwner {
        payable(owner()).transfer(_amount);
    }


    function withdrawToken(address _tokenContract, uint256 _amount) external onlyOwner {
        IERC20 tokenContract = IERC20(_tokenContract);
        tokenContract.transfer(msg.sender, _amount);
    }


    // TESTING
    function see_Dev1_address() public view returns (address) {
        return dev1;
    }

    function see_Dev2_address() public view returns (address) {
        return dev2;
    }

     function see_Dev1_percent() public view returns (uint256) {
        return dev1_percent;
    }

    function see_Dev2_percent() public view returns (uint256) {
        return dev2_percent;
    }


    // Contract Control _ OnlyOwner
    function openAwardState() external onlyOwner {
        require(award_state == AWARD_STATE.CLOSED);
        award_state = AWARD_STATE.OPEN;
    }

    function closeAwardState() external onlyOwner {
        require(award_state == AWARD_STATE.OPEN);
        award_state = AWARD_STATE.CLOSED;
    }

    function setdev1(address payable _address) external  onlyOwner {
        dev1 = _address;
    }

    function setdev2(address payable _address) external onlyOwner {
        dev2 = _address;
    }

    function set_Dev1_percent(uint256 _percent) external onlyOwner {
        require(_percent <= 20);
        dev1_percent  = _percent;
    }

    function set_Dev2_percent(uint256 _percent) external onlyOwner {
        require(_percent <= 20);
        dev2_percent  = _percent;
    }

    function setRewardTokenAddress(address _address) public onlyOwner {
        rewardTokenContract = _address;
    }

    function setRewardTokenDecimals(uint _decimals) public onlyOwner {
        rewardDecimals = _decimals;
    }
}




