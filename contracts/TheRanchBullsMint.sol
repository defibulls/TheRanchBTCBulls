// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*    
🅣🅗🅔🅡🅐🅝🅒🅗_🅑🅤🅛🅛🅢_➋⓿➋➋
*/


import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import { IERC2981, IERC165 } from "@openzeppelin/contracts/interfaces/IERC2981.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

contract TheRanchBullsMint is ERC721Enumerable, IERC2981, Ownable {
    using Strings for uint256;

    using Counters for Counters.Counter;
    Counters.Counter private _tokenSupply;
  
    uint256 public constant NODEBULLS_SALE_TOTAL = 4999;
    uint256 public NODEBULLS_MAX_MINTS_PER_TX = 5;
    uint256 public NODEBULLS_MINT_PRICE = 250;
    uint256 public NODEBULLS_MAX_MINTS_TOTAL_PER_WALLET = 20;
  
   
    mapping(address => bool) public whiteList;
    mapping(address => bool) public presaleList;
    mapping(address => uint256) public addressPurchases;

    string private _tokenBaseURI;
    string private baseURI;
    string private baseExtension = ".json";
 
    bool public presaleLive = false;
    bool public publicSaleLive = false;
    bool public paused = true;
   
    address public royalties;   // will be set as the future_projects wallet 
    address public mintingTokenContract;
    uint public mintingDecimals = 18;


    constructor(
        address _royalties,
        string memory _initBaseURI
    ) public
        ERC721("TheRanch_Bulls", "TRB") {
        royalties = _royalties;
        setBaseURI(_initBaseURI);
    }


    // MINTING
    function mint(uint256 tokenQuantity) external payable {
        require(!paused, "ERROR: Contract Paused. Please Check Discord.");
        require(tokenQuantity > 0, "MINIMUM_ONE_TOKEN_PER_MINT");
        IERC20 mintingToken = IERC20(mintingTokenContract);

        uint256 NODEBULLS_MINT_PRICE = NODEBULLS_MINT_PRICE * 10 ** mintingDecimals;

        if (presaleLive) {
            if (whiteList[msg.sender]) {
                require(addressPurchases[msg.sender] + tokenQuantity <= 5, "EXCEEDS PRESALE AMOUNT");
                require(mintingToken.allowance(msg.sender, address(this)) >= ((NODEBULLS_MINT_PRICE * tokenQuantity) - NODEBULLS_MINT_PRICE),"Insuficient Allowance");
                require(mintingToken.transferFrom(msg.sender, address(this), ((NODEBULLS_MINT_PRICE * tokenQuantity) - NODEBULLS_MINT_PRICE)), "ERROR: PRICE EXCEEDS THE AMT OF USDC PROVIDED ((NODEBULLS_MINT_PRICE * quantity)) - NODEBULLS_MINT_PRICE)");
                for (uint256 i = 0; i < tokenQuantity; i++) {
                    addressPurchases[msg.sender]++;
                    _tokenSupply.increment();
                    _safeMint(msg.sender, _tokenSupply.current());
                }
                
            } else if (presaleList[msg.sender]){
                require(addressPurchases[msg.sender] + tokenQuantity <= 5, "EXCEEDS PRESALE AMOUNT");
                require(mintingToken.allowance(msg.sender, address(this)) >= (NODEBULLS_MINT_PRICE * tokenQuantity),"Insuficient Allowance");
                require(mintingToken.transferFrom(msg.sender, address(this), (NODEBULLS_MINT_PRICE * tokenQuantity)), "ERROR: PRICE EXCEEDS THE AMT OF USDC PROVIDED (NODEBULLS_MINT_PRICE * quantity)");
                for (uint256 i = 0; i < tokenQuantity; i++) {
                    addressPurchases[msg.sender]++;
                    _tokenSupply.increment();
                    _safeMint(msg.sender, _tokenSupply.current());
                }
            } else {
                 require(((whiteList[msg.sender]) || (presaleList[msg.sender])), "ERROR: Only Whitelist And Presale Addresses Can Mint!");
            }
        } else if (publicSaleLive && !presaleLive){
            require(addressPurchases[msg.sender] + tokenQuantity <= NODEBULLS_MAX_MINTS_TOTAL_PER_WALLET, "EXCEEDS MAX AMOUNT PER WALLET");
            require(tokenQuantity <= NODEBULLS_MAX_MINTS_PER_TX, "EXCEEDS_BULLS_PER_TRANSACTION");
            require(_tokenSupply.current() + tokenQuantity <= NODEBULLS_SALE_TOTAL, "EXCEEDS_MAX_MINT");
            require(mintingToken.allowance(msg.sender, address(this)) >= (NODEBULLS_MINT_PRICE * tokenQuantity),"Insuficient Allowance");
            require(mintingToken.transferFrom(msg.sender, address(this), (NODEBULLS_MINT_PRICE * tokenQuantity)), "ERROR: PRICE EXCEEDS THE AMT OF USDC PROVIDED (NODEBULLS_MINT_PRICE * quantity)");
            for(uint256 i = 0; i < tokenQuantity; i++) {
                addressPurchases[msg.sender]++;
                _tokenSupply.increment();
                _safeMint(msg.sender, _tokenSupply.current());
            }
        } else {
            require((presaleLive && !publicSaleLive) || (!presaleLive && publicSaleLive), "ERROR: Minting Is Not Live At This Time.");
        }
    }

    

    function getBalance() public view returns (uint256){
        uint256 _balance = address(this).balance;
        return _balance;
    }


    function checkTokenBalance(address token) public view returns(uint) {
        IERC20 token = IERC20(token);
        return token.balanceOf(address(this));
    }

    function walletOfOwner(address _owner) public view returns (uint256[] memory) {
        uint256 ownerTokenCount = balanceOf(_owner);
        uint256[] memory tokenIds = new uint256[](ownerTokenCount);
        for (uint256 i; i < ownerTokenCount; i++) {
            tokenIds[i] = tokenOfOwnerByIndex(_owner, i);
        }
        return tokenIds;
    }

    function isWhitelisted(address _user) public view returns (bool) {
        if (whiteList[_user]){
            return true;
        }
        return false;
    }

    function isPresalelisted(address _user) public view returns (bool) {
        if (presaleList[_user]){
            return true;
        }
        return false;
    }



    // Contract Funding / Withdrawing / Transferring
    function fund() public payable {}

    function withdraw(uint256 _amount) external onlyOwner {
        payable(owner()).transfer(_amount);
    }

    function withdrawToken(address _tokenContract, uint256 _amount) external onlyOwner {
        IERC20 tokenContract = IERC20(_tokenContract);
        tokenContract.transfer(msg.sender, _amount);
    }


    // PRESALE-WHITELIST 
    function addToWhiteList(address[] calldata entries) external onlyOwner {
        for(uint256 i = 0; i < entries.length; i++) {
            address entry = entries[i];
            require(entry != address(0), "NULL_ADDRESS");
            require(!whiteList[entry], "DUPLICATE_ENTRY");
            whiteList[entry] = true;
        }
    }

    function removeFromWhiteList(address[] calldata entries) external onlyOwner {
        for(uint256 i = 0; i < entries.length; i++) {
            address entry = entries[i];
            require(entry != address(0), "NULL_ADDRESS");
            whiteList[entry] = false;
        }
    }

   function addToPresaleList(address[] calldata entries) external onlyOwner {
        for(uint256 i = 0; i < entries.length; i++) {
            address entry = entries[i];
            require(entry != address(0), "NULL_ADDRESS");
            require(!presaleList[entry], "DUPLICATE_ENTRY");
            presaleList[entry] = true;
        }
    }

    function removeFromPresaleList(address[] calldata entries) external onlyOwner {
        for(uint256 i = 0; i < entries.length; i++) {
            address entry = entries[i];
            require(entry != address(0), "NULL_ADDRESS");
            presaleList[entry] = false;
        }
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
    function togglePresaleStatus() external onlyOwner {
        presaleLive = !presaleLive;
    }

    function togglePublicSaleStatus() external onlyOwner {
        publicSaleLive = !publicSaleLive;
    }

    function togglePauseStatus() external onlyOwner {
        paused = !paused;
    }

    function adjustMintsPerWallet(uint num) external onlyOwner {
        require(num >= 20);
        NODEBULLS_MAX_MINTS_TOTAL_PER_WALLET = num;
    }
    function adjustMintsPerTransaction(uint num) external onlyOwner {
        require(num >= 3);
        NODEBULLS_MAX_MINTS_PER_TX = num;
    }

    function adjustPricePerMint(uint num) external onlyOwner {
        require(num >= 100);
        NODEBULLS_MINT_PRICE = num;
    }

    function setRoyaltyAddress(address _royalties) public onlyOwner {
        royalties = _royalties;
    }

    function setMintingTokenAddress(address _address) public onlyOwner {
        mintingTokenContract = _address;
    }

    function setMintingTokenDecimals(uint _decimals) public onlyOwner {
        mintingDecimals = _decimals;
    }
}




