// // SPDX-License-Identifier: MIT
// pragma solidity ^0.8.0;

// /*    
// 🅣🅗🅔🅡🅐🅝🅒🅗_🅑🅤🅛🅛🅢_➋⓿➋➋
// */


// // Confirm royalties are being paid out. 
// // Confirm the royalies wallet doesn't have to pay royalties on anything that wallet purchases. 
// // DECIMAL variable to help


// import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
// import "@openzeppelin/contracts/access/Ownable.sol";
// import "@openzeppelin/contracts/utils/Counters.sol";
// import { IERC2981, IERC165 } from "@openzeppelin/contracts/interfaces/IERC2981.sol";
// import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
// import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
// import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol";



// contract TheRanchBullsMint is ERC721Enumerable, IERC2981, Ownable {
//     using Strings for uint256;

//     using Counters for Counters.Counter;
//     Counters.Counter private _tokenSupply;
//     Counters.Counter private _airDropSupply;

//     uint256 public constant NODEBULLS_SALE_TOTAL = 4999;    // Total NFT count to sale is NODEBULLS_SALE_TOTAL - NODEBULLS AIRDROP-TOTAL 
//     uint256 public constant NODEBULLS_MAX_MINTS_PER_TX = 5;
//     uint256 public constant NODEBULLS_MINT_PRICE = 250;
//     uint256 public NODEBULLS_MAX_MINTS_TOTAL_PER_WALLET = 20;
  
   
//     mapping(address => bool) public whiteList;
//     mapping(address => bool) public presaleList;
//     mapping(address => uint256) public addressPurchases;

//     string private _tokenBaseURI;
//     string private baseURI;
//     string private baseExtension = ".json";
 
//     bool public presaleLive = false;
//     bool public publicSaleLive = false;
//     bool public paused = true;
   
//     address public royalties;   // will be set as the future_projects wallet 
//     address public mintingTokenContract;
//     uint public mintingDecimals = 18;


//     constructor(
//         address _royalties,
//         string memory _initBaseURI
//     ) public
//         ERC721("TheRanch_Bulls", "TRB") {
//         royalties = _royalties;
//         setBaseURI(_initBaseURI);
//     }


//     // MINTING
//     function mint(uint256 tokenQuantity) external payable {
//         require(!paused, "ERROR: Contract paused. Please check discord.");
//         require(tokenQuantity > 0, "MINIMUM_ONE_TOKEN_PER_MINT");
//         IERC20 mintingToken = IERC20(mintingTokenContract);

//         uint256 NODEBULLS_MINT_PRICE = NODEBULLS_MINT_PRICE * 10 ** mintingDecimals;

//         if (presaleLive) {
//             if (whiteList[msg.sender]) {
//                 require(addressPurchases[msg.sender] + tokenQuantity <= 3, "EXCEEDS PRESALE AMOUNT");
//                 require(mintingToken.allowance(msg.sender, address(this)) >= ((NODEBULLS_MINT_PRICE * tokenQuantity) - NODEBULLS_MINT_PRICE),"Insuficient Allowance");
//                 require(mintingToken.transferFrom(msg.sender, address(this), ((NODEBULLS_MINT_PRICE * tokenQuantity) - NODEBULLS_MINT_PRICE)), "ERROR: PRICE EXCEEDS THE AMT OF USDC PROVIDED ((NODEBULLS_MINT_PRICE * quantity)) - NODEBULLS_MINT_PRICE)");
//                 for (uint256 i = 0; i < tokenQuantity; i++) {
//                     addressPurchases[msg.sender]++;
//                     _tokenSupply.increment();
//                     _safeMint(msg.sender, _tokenSupply.current());
//                 }
                
//             } else if (presaleList[msg.sender]){
//                 require(addressPurchases[msg.sender] + tokenQuantity <= 3, "EXCEEDS PRESALE AMOUNT");
//                 require(mintingToken.allowance(msg.sender, address(this)) >= (NODEBULLS_MINT_PRICE * tokenQuantity),"Insuficient Allowance");
//                 require(mintingToken.transferFrom(msg.sender, address(this), (NODEBULLS_MINT_PRICE * tokenQuantity)), "ERROR: PRICE EXCEEDS THE AMT OF USDC PROVIDED (NODEBULLS_MINT_PRICE * quantity)");
//                 for (uint256 i = 0; i < tokenQuantity; i++) {
//                     addressPurchases[msg.sender]++;
//                     _tokenSupply.increment();
//                     _safeMint(msg.sender, _tokenSupply.current());
//                 }
//             } else {
//                  require(((whiteList[msg.sender]) || (presaleList[msg.sender])), "ERROR: Only Whitelist and Presale addresses can mint!");
//             }
//         } else if (publicSaleLive && !presaleLive){
//             require(addressPurchases[msg.sender] + tokenQuantity <= NODEBULLS_MAX_MINTS_TOTAL_PER_WALLET, "EXCEEDS MAX AMOUNT PER WALLET");
//             require(tokenQuantity <= NODEBULLS_MAX_MINTS_PER_TX, "EXCEEDS_BULLS_PER_TRANSACTION");
//             require(_tokenSupply.current() + tokenQuantity <= NODEBULLS_SALE_TOTAL, "EXCEEDS_MAX_MINT");
//             require(mintingToken.allowance(msg.sender, address(this)) >= (NODEBULLS_MINT_PRICE * tokenQuantity),"Insuficient Allowance");
//             require(mintingToken.transferFrom(msg.sender, address(this), (NODEBULLS_MINT_PRICE * tokenQuantity)), "ERROR: PRICE EXCEEDS THE AMT OF USDC PROVIDED (NODEBULLS_MINT_PRICE * quantity)");
//             for(uint256 i = 0; i < tokenQuantity; i++) {
//                 addressPurchases[msg.sender]++;
//                 _tokenSupply.increment();
//                 _safeMint(msg.sender, _tokenSupply.current());
//             }
//         } else {
//             require(publicSaleLive == true || presaleLive == true, "ERROR: Only Whitelist and Presale addresses can mint!");
//         }
//     }

    

//     function getBalance() public view returns (uint256){
//         uint256 _balance = address(this).balance;
//         return _balance;
//     }


//     function checkTokenBalance(address token) public view returns(uint) {
//         IERC20 token = IERC20(token);
//         return token.balanceOf(address(this));
//     }

//     function walletOfOwner(address _owner) public view returns (uint256[] memory) {
//         uint256 ownerTokenCount = balanceOf(_owner);
//         uint256[] memory tokenIds = new uint256[](ownerTokenCount);
//         for (uint256 i; i < ownerTokenCount; i++) {
//             tokenIds[i] = tokenOfOwnerByIndex(_owner, i);
//         }
//         return tokenIds;
//     }




//     // Contract Funding / Withdrawing / Transferring
//     function fund() public payable {}

//     function withdraw() external onlyOwner {
//         uint _balance = address(this).balance;
//         payable(owner()).transfer(_balance);
//     }

//     function withdrawToken(address _tokenContract, uint256 _amount) external onlyOwner {
//         IERC20 tokenContract = IERC20(_tokenContract);
//         tokenContract.transfer(msg.sender, _amount);
//     }


//     // PRESALE-WHITELIST 
//     function addToWhiteList(address[] calldata entries) external onlyOwner {
//         for(uint256 i = 0; i < entries.length; i++) {
//             address entry = entries[i];
//             require(entry != address(0), "NULL_ADDRESS");
//             require(!whiteList[entry], "DUPLICATE_ENTRY");
//             whiteList[entry] = true;
//         }
//     }

//     function removeFromwhiteList(address[] calldata entries) external onlyOwner {
//         for(uint256 i = 0; i < entries.length; i++) {
//             address entry = entries[i];
//             require(entry != address(0), "NULL_ADDRESS");
//             whiteList[entry] = false;
//         }
//     }

//    function addToPresaleList(address[] calldata entries) external onlyOwner {
//         for(uint256 i = 0; i < entries.length; i++) {
//             address entry = entries[i];
//             require(entry != address(0), "NULL_ADDRESS");
//             require(!presaleList[entry], "DUPLICATE_ENTRY");
//             presaleList[entry] = true;
//         }
//     }

//     function removeFromPresaleList(address[] calldata entries) external onlyOwner {
//         for(uint256 i = 0; i < entries.length; i++) {
//             address entry = entries[i];
//             require(entry != address(0), "NULL_ADDRESS");
//             presaleList[entry] = false;
//         }
//     }



//     // METADATA
//     function _baseURI() internal view virtual override returns (string memory) {
//         return baseURI;
//     }

//     function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
//         require(_exists(tokenId),"ERC721Metadata: URI query for nonexistent token");
      
//         string memory currentBaseURI = _baseURI();
//         return bytes(currentBaseURI).length > 0 ? string(abi.encodePacked(currentBaseURI, tokenId.toString(), baseExtension)) : "";
//     }

//     function setBaseURI(string memory _newBaseURI) public onlyOwner {
//         baseURI = _newBaseURI;
//     }

//     function setBaseExtension(string memory _newBaseExtension) external onlyOwner {
//         baseExtension = _newBaseExtension;
//     }

//     // ERC165
//     function supportsInterface(bytes4 interfaceId) public view override(ERC721Enumerable, IERC165) returns (bool) {
//         return interfaceId == type(IERC2981).interfaceId || super.supportsInterface(interfaceId);
//     }

//     // IERC2981
//     function royaltyInfo(uint256 _tokenId, uint256 _salePrice) external view override returns (address, uint256 royaltyAmount) {
//         _tokenId; // silence solc warning
//         royaltyAmount = (_salePrice / 100) * 5;
//         return (royalties, royaltyAmount);
//     }

//     // Contract Control _ OnlyOwner
//     function togglePresaleStatus() external onlyOwner {
//         presaleLive = !presaleLive;
//     }

//     function adjustMintsPerWallet(uint num) external onlyOwner {
//         require(num >= 20);
//         NODEBULLS_MAX_MINTS_TOTAL_PER_WALLET = num;
//     }

//     function togglePublicSaleStatus() external onlyOwner {
//         publicSaleLive = !publicSaleLive;
//     }

//     function togglePauseStatus() external onlyOwner {
//         paused = !paused;
//     }

//     function setRoyaltyAddress(address _royalties) public onlyOwner {
//         royalties = _royalties;
//     }

//     function setMintingTokenAddress(address _address) public onlyOwner {
//         mintingTokenContract = _address;
//     }

//     function setMintingTokenDecimals(uint _decimals) public onlyOwner {
//         mintingDecimals = _decimals;
//     }

// }






















// contract TheRanchBullsAirDrop is VRFConsumerBase, Ownable {

//     AggregatorV3Interface public priceFeed;
//     mapping(address => uint256) public addressToAmountFunded;


//     address public TheRanchBullsMintAddress;
//     address public dev1;
//     address public dev2;
//     uint256 public dev1_percent = 14;
//     uint256 public dev2_percent = 6;
//     address public royalties;   // will be set as the future_projects wallet 
//     address public rewardTokenContract;
//     uint public rewardDecimals = 18;

//     uint public giveawayId;

//     event centennial_Air_Drop(
//         uint indexed giveawayId,
//         uint256 indexed payout_cut,
//         uint256[] winners   
//     );


//     bytes32 public keyhash;
//     address payable public recentWinner;
//     uint256 public randomResult;
//     event RequestedRandomness(bytes32 requestId);

//     enum AWARD_STATE {
//         OPEN,
//         CLOSED,
//         PAY_AUTHORIZED
//     }
//     AWARD_STATE public award_state;
//     uint256 public fee;


//     constructor(
//         address _dev1,
//         address _dev2,
//         address _vrfCoordinator,
//         address _link,
//         uint256 _fee,
//         bytes32 _keyhash
//     ) public
//         VRFConsumerBase(_vrfCoordinator, _link) {
//         dev1 = _dev1;
//         dev2 = _dev2;
//         award_state = AWARD_STATE.CLOSED;
//         fee = _fee;
//         keyhash = _keyhash;    
//     }

//     // CHAINLINK
//     /** 
//      * Requests randomness from Chainlink
//      */
//     function getRandomNumber() public returns (bytes32 requestId) {
//         require(LINK.balanceOf(address(this)) >= fee, "Not enough LINK - fill contract with more");
//         bytes32 requestId = requestRandomness(keyhash, fee);
//         emit RequestedRandomness(requestId);
//         return requestId;
//     }


//     /**
//      * Callback function used by VRF Coordinator
//      */
//     function fulfillRandomness(bytes32 requestId, uint256 randomness) internal override {
//         randomResult = randomness;
//     }

//     /**
//      * Expand the single random number from the VRF into more (n) 
//     */
//     function expand(uint256 randomValue, uint256 n) public returns (uint256[] memory expandedValues) {

//         // get the tokenBalance from the minting contract as 
//         uint tokenSupply = 200;
//         require(n <= tokenSupply, "Looking for too many results, this will infinitely loop");
//         expandedValues = new uint256[](n);
//         uint found_num;
//         uint i = 0;
//         while (found_num < n) {
//             uint256 num = (uint256(keccak256(abi.encode(randomValue, i))) % tokenSupply);
//             if (num != 0 && num <= tokenSupply && exists(expandedValues,num) == false) {
//                 expandedValues[found_num] = num;
//                 found_num++;
//             }
//             i++;
//         }
//         require(expandedValues.length == 100, "We didn't find 100 winners during the expansion");
//         // weeklyWinners = expandedValues;
//         award_state = AWARD_STATE.PAY_AUTHORIZED;
//         return expandedValues;
//     }

//     /**
//      * Assist the expand function to limit the same number twice 
//     */
//     function exists (uint256[] memory arrayToCheck, uint numberToCheck) internal returns (bool) {
//         for (uint i = 0; i < arrayToCheck.length; i++) {
//             if (arrayToCheck[i] == numberToCheck) {
//                 return true;
//             }
//         }
//         return false;
//     }


//     // REWARDING of the 100 Bulls after paying out the DEV team
//     function centennialAirDrop() public onlyOwner {
//         require(award_state == AWARD_STATE.OPEN, "The award state is currently closed");
//         require(checkTokenBalance(rewardTokenContract)>= 100 * 10 ** rewardDecimals, "Not Enough Funds to Warrant calling the function to award the Bulls");
//         require(award_state == AWARD_STATE.OPEN, "ERROR: The Award function is not open.");
//         require(dev1_percent + dev2_percent <= 20, "Dev1 Percent + Dev2 Percent must be lower than 20%");
        
        
//         // require(_tokenSupply.current() >= 100);

//         IERC20 tokenContract = IERC20(rewardTokenContract);

//         uint256 _balance = checkTokenBalance(rewardTokenContract);
//         tokenContract.transfer(dev1, _balance * dev1_percent / 100);
//         tokenContract.transfer(dev2, _balance * dev2_percent / 100);

//         _balance = checkTokenBalance(rewardTokenContract);
//         uint256 centennial_cut = _balance / 100;

//         getRandomNumber();
//         uint256[] memory weeklyWinners = expand(randomResult,100); 

//         require(award_state == AWARD_STATE.PAY_AUTHORIZED);
        
//         // for (uint256 i = 0; i < weeklyWinners.length; i++) {
//         //     uint winning_index = weeklyWinners[i];
//         //     address luckyBull = ownerOf(winning_index);
//         //     tokenContract.transfer(luckyBull, centennial_cut);
//         // }

//         // emit centennial_Air_Drop(giveawayId, centennial_cut, weeklyWinners);

//         giveawayId++;
//         award_state = AWARD_STATE.CLOSED;

//     }





//     //INFO RETURN


//     function setTheRanchBullsMintAddress(address _mintAddress) external {
//         TheRanchBullsMintAddress = _mintAddress;
//     }

//     function getTotalSupply() external view returns (uint) {
//         TheRanchBullsMint TRBM = TheRanchBullsMint(TheRanchBullsMintAddress);
//         return TRBM.totalSupply();

//     }



//     function getLinkBalance() public view returns (uint256){
//         uint256 _balance = LINK.balanceOf(address(this));
//         return _balance;
//     }

//     function getBalance() public view returns (uint256){
//         uint256 _balance = address(this).balance;
//         return _balance;
//     }

//     function getRandomResult() public view returns (uint256){
//         return randomResult;
//     }

//     function checkTokenBalance(address token) public view returns(uint) {
//         IERC20 token = IERC20(token);
//         return token.balanceOf(address(this));
//     }



//     // Contract Funding / Withdrawing / Transferring
//     function fund() public payable {
//         addressToAmountFunded[msg.sender] += msg.value;
//     }

//     function withdraw() external onlyOwner {
//         uint _balance = address(this).balance;
//         payable(owner()).transfer(_balance);
//     }

//     function withdrawToken(address _tokenContract, uint256 _amount) external onlyOwner {
//         IERC20 tokenContract = IERC20(_tokenContract);
//         tokenContract.transfer(msg.sender, _amount);
//     }


//     // TESTING
//     function see_Dev1_address() public view returns (address) {
//         return dev1;
//     }

//     function see_Dev2_address() public view returns (address) {
//         return dev2;
//     }

//      function see_Dev1_percent() public view returns (uint256) {
//         return dev1_percent;
//     }

//     function see_Dev2_percent() public view returns (uint256) {
//         return dev2_percent;
//     }


//     // Contract Control _ OnlyOwner
//     function openAwardState() external onlyOwner {
//         award_state = AWARD_STATE.OPEN;
//     }

//     function closeAwardState() external onlyOwner {
//         award_state = AWARD_STATE.CLOSED;
//     }

//     function setdev1(address payable _address) external  onlyOwner {
//         dev1 = _address;
//     }

//     function setdev2(address payable _address) external onlyOwner {
//         dev2 = _address;
//     }

//     function set_Dev1_percent(uint256 _percent) external onlyOwner {
//         require(_percent <= 20);
//         dev1_percent  = _percent;
//     }

//     function set_Dev2_percent(uint256 _percent) external onlyOwner {
//         require(_percent <= 20);
//         dev2_percent  = _percent;
//     }

//     function setRewardTokenAddress(address _address) public onlyOwner {
//         rewardTokenContract = _address;
//     }

//     function setRewardTokenDecimals(uint _decimals) public onlyOwner {
//         rewardDecimals = _decimals;
//     }
// }






