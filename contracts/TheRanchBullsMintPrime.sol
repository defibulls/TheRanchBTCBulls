// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*    
🅣🅗🅔🅡🅐🅝🅒🅗_🅑🅤🅛🅛🅢_➋⓿➋➋
*/


import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import { IERC2981, IERC165 } from "@openzeppelin/contracts/interfaces/IERC2981.sol";



contract TheRanchBullsMintPrime is ERC721Enumerable, IERC2981, Ownable {
    using Strings for uint256;

    using Counters for Counters.Counter;
    Counters.Counter private _tokenSupply;
    
    AggregatorV3Interface internal maticUsdPriceFeed;
    uint256 public constant NODEBULLS_SALE_TOTAL = 4999;
    uint256 public constant WHITELIST_TOTAL = 30;
    uint256 public NODEBULLS_MAX_MINTS_TOTAL_PER_WALLET = 100;
    uint256 public ORDER_QUANTITY_1 = 200;
    uint256 public ORDER_QUANTITY_2 = 180;
    uint256 public ORDER_QUANTITY_3 = 170;
    uint256 public ORDER_QUANTITY_5 = 160;
    uint256 public ORDER_QUANTITY_7 = 150;
    uint256 public ORDER_QUANTITY_11 = 140;

    
    mapping(address => uint256) public addressPurchases;

    string private _tokenBaseURI;
    string private baseURI;
    string private baseExtension = ".json";
 
    bool public publicSaleLive = false;
    bool public paused = true;
   
    address public royalties;   // will be set as the future_projects wallet 

    constructor(
        address _priceFeedAddress,
        address _royalties,
        string memory _initBaseURI
    ) public
        ERC721("TheRanch_Bulls", "TRB") {
        royalties = _royalties;
        setBaseURI(_initBaseURI);
        maticUsdPriceFeed = AggregatorV3Interface(_priceFeedAddress);

        for(uint256 i = 0; i < WHITELIST_TOTAL; i++) {
                _tokenSupply.increment();
                _safeMint(msg.sender, _tokenSupply.current());
        }
    }

    uint[] allowedTokenQuantity = [1,2,3,5,7,11];
    // MINTING
    function mint(uint256 tokenQuantity) external payable {
        require(!paused, "ERROR: Contract Paused. Please Check Discord.");
        require(publicSaleLive, "ERROR: PUBLIC MINTING HAS NOT STARTED Paused. Please Check Discord.");
        require(tokenQuantity > 0, "MINIMUM_ONE_TOKEN_PER_MINT");
        require(isAllowedTokenQuantity(tokenQuantity), "You must select an amount equal to 1,3,5,7,11");
        require(_tokenSupply.current() + tokenQuantity <= NODEBULLS_SALE_TOTAL, "EXCEEDS_OUR_MAX_NFT_COUNT AT 4999");
        require(addressPurchases[msg.sender] + tokenQuantity <= NODEBULLS_MAX_MINTS_TOTAL_PER_WALLET, "EXCEEDS MAX AMOUNT PER WALLET");

        if (tokenQuantity == 1) {
            require(msg.value >= (getMintPrice(ORDER_QUANTITY_1) * tokenQuantity), "ERROR: PRICE EXCEEDS THE AMT PROVIDED (NODEBULLS_MINT_PRICE * quantity)");
            for(uint256 i = 0; i < tokenQuantity; i++) {
                addressPurchases[msg.sender]++;
                _tokenSupply.increment();
                _safeMint(msg.sender, _tokenSupply.current());
            }
        } else if (tokenQuantity == 2) {
            require(msg.value >= (getMintPrice(ORDER_QUANTITY_2) * tokenQuantity), "ERROR: PRICE EXCEEDS THE AMT PROVIDED (NODEBULLS_MINT_PRICE * quantity)");
            for(uint256 i = 0; i < tokenQuantity; i++) {
                addressPurchases[msg.sender]++;
                _tokenSupply.increment();
                _safeMint(msg.sender, _tokenSupply.current());
            }
        } else if (tokenQuantity == 3) {
            require(msg.value >= (getMintPrice(ORDER_QUANTITY_3) * tokenQuantity), "ERROR: PRICE EXCEEDS THE AMT PROVIDED (NODEBULLS_MINT_PRICE * quantity)");
            for(uint256 i = 0; i < tokenQuantity; i++) {
                addressPurchases[msg.sender]++;
                _tokenSupply.increment();
                _safeMint(msg.sender, _tokenSupply.current());
            }
        } else if (tokenQuantity == 5) {
            require(msg.value >= (getMintPrice(ORDER_QUANTITY_5) * tokenQuantity), "ERROR: PRICE EXCEEDS THE AMT PROVIDED (NODEBULLS_MINT_PRICE * quantity)");
            for(uint256 i = 0; i < tokenQuantity; i++) {
                addressPurchases[msg.sender]++;
                _tokenSupply.increment();
                _safeMint(msg.sender, _tokenSupply.current());
            }
        } else if (tokenQuantity == 7) {
            require(msg.value >= (getMintPrice(ORDER_QUANTITY_7) * tokenQuantity), "ERROR: PRICE EXCEEDS THE AMT PROVIDED (NODEBULLS_MINT_PRICE * quantity)");
            for(uint256 i = 0; i < tokenQuantity; i++) {
                addressPurchases[msg.sender]++;
                _tokenSupply.increment();
                _safeMint(msg.sender, _tokenSupply.current());
            }
        } else if (tokenQuantity == 11) {
            require(msg.value >= (getMintPrice(ORDER_QUANTITY_11) * tokenQuantity), "ERROR: PRICE EXCEEDS THE AMT PROVIDED (NODEBULLS_MINT_PRICE * quantity)");
            for(uint256 i = 0; i < tokenQuantity; i++) {
                addressPurchases[msg.sender]++;
                _tokenSupply.increment();
                _safeMint(msg.sender, _tokenSupply.current());
            }
        }
     
    }


    function isAllowedTokenQuantity(uint256 num) public view returns (bool) {
        for (uint i = 0; i < allowedTokenQuantity.length; i++) {
            if (allowedTokenQuantity[i] == num) {
                return true;
            }
        }
        return false;
    }


    function getMintPrice(uint _amount) public view returns (uint256) {
        (, int256 price, , , ) = maticUsdPriceFeed.latestRoundData();
        uint256 adjustedPrice = uint256(price) * 10**10; // 18 decimals
        uint256 cost = ((_amount * 10**18) * 10**18) / adjustedPrice;
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

    function withdraw(uint256 _amount) external onlyOwner {
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
        royaltyAmount = (_salePrice / 100) * 5;
        return (royalties, royaltyAmount);
    }

    // Contract Control _ OnlyOwner
    function togglePublicSaleStatus() external onlyOwner {
        publicSaleLive = !publicSaleLive;
    }

    function togglePauseStatus() external onlyOwner {
        paused = !paused;
    }

    function adjustMintsPerWallet(uint num) external onlyOwner {
        NODEBULLS_MAX_MINTS_TOTAL_PER_WALLET = num;
    }
   
    function setRoyaltyAddress(address _royalties) public onlyOwner {
        royalties = _royalties;
    }

    function setPriceFeedAddress(address _address) public onlyOwner {
        maticUsdPriceFeed = AggregatorV3Interface(_address);
    }

    function SET_ORDER_QUANTITY_1(uint num) external onlyOwner {
        ORDER_QUANTITY_1 = num;
    }

    function SET_ORDER_QUANTITY_2(uint num) external onlyOwner {
        ORDER_QUANTITY_2 = num;
    }

    function SET_ORDER_QUANTITY_3(uint num) external onlyOwner {
        ORDER_QUANTITY_3 = num;
    }
    
    function SET_ORDER_QUANTITY_5(uint num) external onlyOwner {
        ORDER_QUANTITY_5 = num;
    }
    
    function SET_ORDER_QUANTITY_7(uint num) external onlyOwner {
        ORDER_QUANTITY_7 = num;
    }
    
    function SET_ORDER_QUANTITY_11(uint num) external onlyOwner {
        ORDER_QUANTITY_11 = num;
    }

    // OVERRIDE FUNCTIONALITY
    function transferOwnership(address newOwner) public virtual override onlyOwner{
        // DO NOTHING
    }

}




