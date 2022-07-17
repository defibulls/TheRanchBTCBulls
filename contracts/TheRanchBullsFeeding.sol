// SPDX-License-Identifier: MIT
pragma solidity 0.8.7;

/*    
🅣🅗🅔🅡🅐🅝🅒🅗_🅑🅤🅛🅛🅢_➋⓿➋➋
*/


import "@openzeppelin/security/ReentrancyGuard.sol";
import "@openzeppelin/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/access/Ownable.sol";
import "@openzeppelin/utils/Counters.sol";
import "@openzeppelin/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/token/ERC20/IERC20.sol";
import { IERC2981, IERC165 } from "@openzeppelin/interfaces/IERC2981.sol";
import "./TheRanchBTCBullsCommunity.sol";



contract TheRanchBullsFeeding is 
    ERC721Enumerable,
    IERC2981,
    Ownable,
    ReentrancyGuard {
    
    using Strings for uint256;
    using SafeERC20 for IERC20;
    using Counters for Counters.Counter;
    Counters.Counter private _tokenSupply;

    address public usdcTokenContract;
    address public TheRanchBullsMintRewardAddress;
    uint public usdcTokenDecimals = 6;

    // coreTeam Addresses
    address public coreTeam_1;

    // Minting 
    uint256 public mintingCost = 100;  // USDC.e
    uint public nftTotalCount = 10000;

    bool public publicSaleLive = false;
    bool public paused = true;

    mapping(address => uint) public userMintCount;  // How many bulls did an address mint


    // NFT INFO 
    string private _tokenBaseURI;
    string private baseURI;
    string private baseExtension = ".json";
 


    event feedBullsEvent(
            uint256 indexed _totalAmountDeposit,
            uint indexed _totalCountOfNfts,
            uint indexed _payPerNFT
    );

  

    constructor(
        string memory _initBaseURI

    ) 
        ERC721("TheRanch_BTC_BULLS", "TRBB") {
        setBaseURI(_initBaseURI);  
    }


   // MINTING
    /**
     * @dev This is the function does the following things:
     * 0. Only works if the raffle is NOT PROCESSING, This only happens once a day for a small amount of time. 
     * 1. Allows users to mint new NFTs 1 - 10 per tx 
     * 2. Updates Mapping for their total count of mints
     * 3. Uses a referral/partners system to see who gets the referral bonus.
     * 4. Enters user into the daily raffle if they chose to do so. 
     * 5. If msg.sender elects to enter raffle, 95% goes to btcMinersFund, if they do not, 98% does. 
    */
    function mint(uint256 _tokenQuantity) public payable {
        // if (paused) { revert Contract_ContractPaused_CheckSocials();}
        // if (!publicSaleLive) { revert Minting_PublicSaleNotLive();}

        if (_tokenSupply.current() + _tokenQuantity > nftTotalCount) {revert Minting_ExceedsTotalBulls();}


        IERC20 usdcToken = IERC20(usdcTokenContract);
        uint256 minting_cost_per_bull = mintingCost * 10 ** usdcTokenDecimals;
    
        uint256 totalTransactionCost = minting_cost_per_bull * _tokenQuantity;
        //require(msg.value == totalTransactionCost, "msg.value not equal to total minting transaction cost.");
        usdcToken.safeTransferFrom(msg.sender, address(this), (totalTransactionCost));

        for(uint256 i = 0; i < _tokenQuantity; i++) {
            _tokenSupply.increment();
            _safeMint(msg.sender, _tokenSupply.current());
        }

        //update the mint count for msg.sender
        userMintCount[msg.sender] += _tokenQuantity;
    }


    // // ONE BY ONE CALL 

    // function feedTheBulls(uint _startingIndex, uint _endingIndex, uint256 _totalAmountToDeposit) public payable onlyOwner {
    
    //     require(_startingIndex < _endingIndex,"ERROR: Start must be lower");
    //     require(_startingIndex > 0,"ERROR: Index 0 doesn't exist");
    //     require(_endingIndex <= _tokenSupply.current(),"ERROR: This touches an non existent NFT ID");
    //     require(address(TheRanchBullsMintRewardAddress) != address(0), "ERROR: TheRanchBullsMintAndReward Address must be set first.");
       
    //     // Transfer rewardTokens to the contract
    //     IERC20 tokenContract = IERC20(usdcTokenContract);
    //     //tokenContract.safeTransferFrom(msg.sender, TheRanchBullsMintAndRewardAddress, _totalAmountToDeposit);
    //     //tokenContract.safeTransferFrom(TheRanchBullsMintAndRewardAddress,msg.sender, _totalAmountToDeposit);
    //     tokenContract.safeTransfer(msg.sender, _totalAmountToDeposit);
    //     //tokenContract.safeTransferFrom(address(this), TheRanchBullsMintAndRewardAddress, _totalAmountToDeposit);


    //     uint256 _payoutCut = _totalAmountToDeposit / _tokenSupply.current();

    //     for( uint i = _startingIndex; i <= _endingIndex; i++) {
    //         address _hayBaleOwner = ownerOf(i);
    //         if (_hayBaleOwner != address(0)){
    //             updatingUsdcToBullsMintandRewardContract(_hayBaleOwner, _payoutCut);
    //         }
    //     }

    // }


    // function updatingUsdcToBullsMintandRewardContract(address _recipient, uint256 _amountToAdd) public {
    //     TheRanchBullsMintReward TRBB = TheRanchBullsMintReward(TheRanchBullsMintRewardAddress);
    //     TRBB.updateUsdcBonusFromAnotherContract(_recipient, _amountToAdd);
    // }





    // pass over an array to the other contract to work with

    function feedTheBulls(uint _startingIndex, uint _endingIndex, uint256 _totalAmountToDeposit) public payable onlyOwner {
    
        require(_startingIndex < _endingIndex,"ERROR: Start must be lower");
        require(_startingIndex > 0,"ERROR: Index 0 doesn't exist");
        require(_endingIndex <= _tokenSupply.current(),"ERROR: This touches an non existent NFT ID");
        require(address(TheRanchBullsMintRewardAddress) != address(0), "ERROR: TheRanchBullsMintAndReward Address must be set first.");
       
        // Transfer rewardTokens to the contract
        IERC20 tokenContract = IERC20(usdcTokenContract);
        //tokenContract.safeTransferFrom(msg.sender, TheRanchBullsMintAndRewardAddress, _totalAmountToDeposit);
        //tokenContract.safeTransferFrom(TheRanchBullsMintAndRewardAddress,msg.sender, _totalAmountToDeposit);
        tokenContract.safeTransfer(msg.sender, _totalAmountToDeposit);
        //tokenContract.safeTransferFrom(address(this), TheRanchBullsMintAndRewardAddress, _totalAmountToDeposit);



        address[] memory haybaleOwners = new address[](_endingIndex); 
   
        uint256 _payoutCut = _totalAmountToDeposit / _tokenSupply.current();
        uint _counter;
        for( uint i = _startingIndex; i <= _endingIndex; i++) {
            address _hayBaleOwner = ownerOf(i);
            if (_hayBaleOwner != address(0)){
                haybaleOwners[_counter] = _hayBaleOwner;
                _counter++;
            }
        }

        updatingUsdcToBullsMintandRewardContract(haybaleOwners, _payoutCut);

        emit feedBullsEvent(_totalAmountToDeposit, ((_endingIndex - _startingIndex)+1), _payoutCut);
    }


    function updatingUsdcToBullsMintandRewardContract(address[] memory _recipients, uint256 _amountToAdd) public {
        TheRanchBTCBullsCommunity TRBC = TheRanchBTCBullsCommunity(TheRanchBullsMintRewardAddress);
        TRBC.updateUsdcBonusFromAnotherContract(_recipients, _amountToAdd);
    }

    


    // Contract Funding / Withdrawing / Transferring
    function fund() public payable {}

    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    function withdrawToken(address _tokenContract, uint256 _amount) external onlyOwner {
        IERC20 tokenContract = IERC20(_tokenContract);
        tokenContract.safeTransfer(msg.sender, _amount);
    }




    /** Getter Functions */

    function getMintCountForAddress(address _address) public view returns (uint) {
        return userMintCount[_address];
    }


    function walletOfOwner(address _owner) public view returns (uint256[] memory) {
        uint256 ownerTokenCount = balanceOf(_owner);
        uint256[] memory tokenIds = new uint256[](ownerTokenCount);
        for (uint256 i; i < ownerTokenCount; i++) {
            tokenIds[i] = tokenOfOwnerByIndex(_owner, i);
        }
        return tokenIds;
    }

 

   // METADATA
    function _baseURI() internal view virtual override returns (string memory) {
        return baseURI;
    }

    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(_exists(tokenId),"ERC721Metadata: URI query for nonexistent token");
        string memory currentBaseURI = _baseURI();
        return bytes(currentBaseURI).length > 0 ? string(abi.encodePacked(currentBaseURI, tokenId.toString(), baseExtension)) : "";
    }

    // ERC165
    function supportsInterface(bytes4 interfaceId) public view override(ERC721Enumerable, IERC165) returns (bool) {
        return interfaceId == type(IERC2981).interfaceId || super.supportsInterface(interfaceId);
    }

    // IERC2981
    function royaltyInfo(uint256 _tokenId, uint256 _salePrice) external view override returns (address, uint256 royaltyAmount) {
        _tokenId; // silence solc warning
        royaltyAmount = _salePrice * 10 / 100;  // 10%
        return (coreTeam_1, royaltyAmount);
    }


    // Contract Control _ OnlyOwner
    function setBaseURI(string memory _newBaseURI) public onlyOwner {
            baseURI = _newBaseURI;
    }


    function setBaseExtension(string memory _newBaseExtension) external onlyOwner {
            baseExtension = _newBaseExtension;
    }


    function togglePublicSaleStatus() external onlyOwner {
        require(address(usdcTokenContract) != address(0), "ERROR: The usdcTokenContract address must be set prior to any minting");
        publicSaleLive = !publicSaleLive;
    }

    function togglePauseStatus() external onlyOwner {
        paused = !paused;
    }

    function setCoreTeam_1_Address(address _coreTeam_1) public onlyOwner {
        require(address(_coreTeam_1) != address(0), "ERROR: The coreTeam_1 address can't be address(0)");
        coreTeam_1 = _coreTeam_1;
    }


    function setMintingPrice(uint _price) external onlyOwner {
        require(paused, "ERROR: CANT CHANGE PRICE IF CONTRACT IS NOT PAUSED");
        mintingCost = _price;
    }

    function setUsdcTokenAddress(address _address) public onlyOwner {
        require(address(_address ) != address(0), "ERROR: The USDC contract address can't be address(0)");
        usdcTokenContract = _address;
    }

    function setUsdcTokenDecimals(uint _decimals) public onlyOwner {
        usdcTokenDecimals = _decimals;
    }


    function setTheRanchBullsMintRewardAddress(address _address) public onlyOwner {
        require(address(_address) != address(0), "ERROR: The mint and reward contract address can't be address(0)");
        TheRanchBullsMintRewardAddress = _address;
    }


}


