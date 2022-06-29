// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;

/*    
🅣🅗🅔🅡🅐🅝🅒🅗_🅑🅤🅛🅛🅢_➋⓿➋➋
*/

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import { IERC2981, IERC165 } from "@openzeppelin/contracts/interfaces/IERC2981.sol";

import "./valhalla.sol";

contract TheRanchBullsMintValhalla is ERC721Enumerable, IERC2981, Ownable {
    using Strings for uint256;

    using Counters for Counters.Counter;
    Counters.Counter private _tokenSupply;
    
    AggregatorV3Interface internal maticUsdPriceFeed;

    uint256 public mintingCost = 150;  // represented in USD value via a pricefeed
    uint public bulls_in_existence = 2000;
    uint public stockYardSize = 5;
    uint public activeStockYardCount = 0;
  
    
    mapping(address => uint256) public addressPurchases;

    string private _tokenBaseURI;
    string private baseURI;
    string private baseExtension = ".json";
 
    bool public publicSaleLive = false;
    bool public paused = true;
   
    address public royalties;
    address public valhallaContractAddress;

    constructor(
        address _royalties,
        address _priceFeedAddress,
        string memory _initBaseURI
    ) public
        ERC721("TheRanch_BTC_BULLS", "TRBB") {
        setBaseURI(_initBaseURI);
        maticUsdPriceFeed = AggregatorV3Interface(_priceFeedAddress);
        require(address(_royalties) != address(0));
        royalties = _royalties;

    }

    // MINTING
    function mint(uint256 tokenQuantity) external payable {
        require(!paused, "ERROR: Contract Paused. Please Check Discord.");
        require(publicSaleLive, "ERROR: PUBLIC MINTING HAS NOT STARTED Paused. Please Check Discord.");
        require(address(royalties) != address(0), "ERROR: The Royalties address must be set prior to any minting");
        require(tokenQuantity > 0, "MINIMUM_ONE_TOKEN_PER_MINT");
        require(tokenQuantity <= 20, "THE MAX YOU CANT MINT IN A SINGLE TX IS 20");
        require(_tokenSupply.current() + tokenQuantity <= bulls_in_existence, "EXCEEDS THE AMOUNT OF BULLS IN EXISTENCE CURRENTLY");

        // require(msg.value >= (getMintPrice(mintingCost) * tokenQuantity), "ERROR: PRICE EXCEEDS THE AMT PROVIDED (mintingCost * quantity)");
        require(msg.value >= (mintingCost * tokenQuantity), "ERROR: PRICE EXCEEDS THE AMT PROVIDED (BULLS_MINT_PRICE * quantity)");
        
        for(uint256 i = 0; i < tokenQuantity; i++) {
            addressPurchases[msg.sender]++;
            _safeMint(msg.sender, _tokenSupply.current());
            _tokenSupply.increment();
        }

        if ((_tokenSupply.current() / stockYardSize) != activeStockYardCount) {
            activeStockYardCount = _tokenSupply.current() / stockYardSize;
        }
    }

    function getValhallaBalance() public view returns (uint256) {
        valhalla VC = valhalla(valhallaContractAddress);
        return VC.getBalance();
    }




























    function setValhallaAddress(address _valhallaAddress) public onlyOwner {
            require(address(_valhallaAddress) != address(0));
            valhallaContractAddress = _valhallaAddress;
        }

    function getMintPrice(uint _amount) public view returns (uint256) {
        (, int256 price, , , ) = maticUsdPriceFeed.latestRoundData();
        uint256 adjustedPrice = uint256(price) * 10**10; // 18 decimals
        uint256 cost = ((_amount * 10**18) * 10**18) / adjustedPrice;     //10**18 == dollar , 10**16 == penny
        return cost;
    }

    function getBalance() public view returns (uint256){
        uint256 _balance = address(this).balance;
        return _balance;
    }

    function walletOfOwner(address _owner) public view returns (uint256[] memory) {
        uint256 ownerTokenCount = balanceOf(_owner);
        uint256[] memory tokenIds = new uint256[](ownerTokenCount);
        for (uint256 i; i < ownerTokenCount; i++) {
            tokenIds[i] = tokenOfOwnerByIndex(_owner, i);
        }
        return tokenIds;
    }

    // Contract Funding / Withdrawing / Transferring
    function fund() public payable {}

    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
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

    function setBaseURI(string memory _newBaseURI) public onlyOwner {
        baseURI = _newBaseURI;
    }

    function setBaseExtension(string memory _newBaseExtension) external onlyOwner {
        baseExtension = _newBaseExtension;
    }

    // ERC165
    function supportsInterface(bytes4 interfaceId) public view override(ERC721Enumerable, IERC165) returns (bool) {
        return interfaceId == type(IERC2981).interfaceId || super.supportsInterface(interfaceId);
    }

    // IERC2981
    function royaltyInfo(uint256 _tokenId, uint256 _salePrice) external view override returns (address, uint256 royaltyAmount) {
        _tokenId; // silence solc warning
        royaltyAmount = _salePrice * 10 / 100;  // 10%
        return (royalties, royaltyAmount);
    }

    // Contract Control _ OnlyOwner
    function togglePublicSaleStatus() external onlyOwner {
        publicSaleLive = !publicSaleLive;
    }

    function togglePauseStatus() external onlyOwner {
        paused = !paused;
    }

    function setRoyaltyAddress(address _royalties) public onlyOwner {
        require(address(_royalties) != address(0), "ERROR: The Royalties address can't be address(0)");
        royalties = _royalties;
    }

    function setPriceFeedAddress(address _address) public onlyOwner {
        maticUsdPriceFeed = AggregatorV3Interface(_address);
    }

    function set_minting_price(uint _price) external onlyOwner {
        require(paused, "ERROR: CANT CHANGE PRICE IF CONTRACT IS NOT PAUSED");
        mintingCost = _price;
    }
}


