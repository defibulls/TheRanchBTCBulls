// // SPDX-License-Identifier: MIT
// pragma solidity 0.8.0;

// /*    
// 🅣🅗🅔🅡🅐🅝🅒🅗_🅑🅤🅛🅛🅢_➋⓿➋➋
// */

// import "@openzeppelin/contracts/access/Ownable.sol";
// import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
// import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// import "./TheRanchBullsMint.sol";

// contract TheRanchBullsReward is Ownable, ReentrancyGuard {
//     using SafeERC20 for IERC20;

//     address public TheRanchBullsMintAddress;
//     address public rewardTokenContract;
//     uint public rewardDecimals = 8;
//     uint256 public eligibleRewardAmount = 0;

//     address public coreteam_1;
//     uint256 public coreteam_1_percent = 8;
//     address public coreteam_2;
//     uint256 public coreteam_2_percent = 2;
    
//     mapping (uint => address) public approvedStockYardWalletAddresses;
//     mapping (uint => uint256) public stockYardRewardBalanceTotal;
//     mapping (uint => mapping (address => uint256)) public stockYardRewardBalancesNftOwners;


//     event withdrawRewardsEvent(
//         address indexed nftOwner,
//         uint256[] stockYardBalances,
//         uint256 indexed totalAmountTransferred
//     );

//     event fundStockyardEvent(
//         uint indexed stockYard,
//         uint256 indexed totalAmountFunded
//     );


//     constructor() public {}

 
//     // Contract Funding
//     function fund(uint256 _amount) public payable {}


//     function fundStockYardAndRewardBulls(uint _stockYardNumber, uint256 _amount) public {
//         require(approvedStockYardWalletAddresses[_stockYardNumber] == msg.sender, "ERROR: You must deposit funds with the correct wallet address");
//         require(address(coreteam_1) != address(0), "ERROR: The coreteam_1 address must be set prior funding");
//         require(address(coreteam_2) != address(0), "ERROR: The coreteam_2 address must be set prior funding");

//         IERC20 tokenContract = IERC20(rewardTokenContract);
//         // Transfer rewardTokens to the contract
//         tokenContract.safeTransferFrom(msg.sender, address(this), _amount);

//         // transfer 10% to coreteam
//         tokenContract.safeTransfer(coreteam_1, _amount * coreteam_1_percent / 100);
//         tokenContract.safeTransfer(coreteam_2, _amount * coreteam_2_percent / 100);

//         // update the total value in each stockyard
//         uint256 rewardBalance = _amount * (100 - (coreteam_1_percent + coreteam_2_percent)) / 100; 
//         stockYardRewardBalanceTotal[_stockYardNumber] += rewardBalance;

//         // update the eligible rewards that each wallet should get if they are apart of this stockyard.
//         uint stockYardSize = getStockYardSize();
//         uint256 payout_per_nft = rewardBalance / stockYardSize;

//         for (uint i = ((stockYardSize * _stockYardNumber) - stockYardSize); i < ((stockYardSize) * _stockYardNumber); i++ ) {
//             address BullOwner = getNFTOwnerOf(i);
//             if (BullOwner != address(0)){
//                 updateNftOwnerRewardBalanceForStockYard(_stockYardNumber,BullOwner,payout_per_nft);
//             } 
//         }

//         // emit event
//         emit fundStockyardEvent(_stockYardNumber,_amount);
//     }



//     function updateNftOwnerRewardBalanceForStockYard(uint _stockYardNumber, address _ownerOfNFT, uint256 _amount) internal {
//         stockYardRewardBalancesNftOwners[_stockYardNumber][_ownerOfNFT] +=  _amount;
//     }

    
//     // Withdrawing 
//     function withdraw() external onlyOwner {
//         payable(owner()).transfer(address(this).balance);
//     }


//     function withdrawToken(address _tokenContract, uint256 _amount) external onlyOwner {
//         IERC20 tokenContract = IERC20(_tokenContract);
//         tokenContract.safeTransfer(msg.sender, _amount);
//     }


//    function withdrawStockYardRewardBalancesForWalletAddress(address _ownerOfNFT) external nonReentrant returns (uint256[] memory) {
//         // Get the total Balance to award the owner of the NFT(s)
//         uint256 balance = getTotalStockYardRewardBalanceForWalletAddress(_ownerOfNFT);
//         require(balance > 0, "You must have a balance more than 0");
        
//         uint256[] memory stockYardBalances = getStockYardRewardBalancesForWalletAddress(_ownerOfNFT);

//         // Transfer Balance 
//         IERC20(rewardTokenContract).safeTransfer(_ownerOfNFT, balance);

//         // Determine how many stockyards we should loop over to change value to zero
//         uint stockYardsToCheck = getActiveStockYardCount();
    
//         // Loop over stockyards and append to stockYardRewardBalances for the nft owner
//         for (uint i; i < stockYardsToCheck; i++) {
//             stockYardRewardBalancesNftOwners[i + 1][_ownerOfNFT] = 0;
//         }

//         // update the total balance for each stockyard
//         for (uint i; i < stockYardsToCheck; i++) {
//             stockYardRewardBalanceTotal[i + 1] -= stockYardBalances[i];
//         }
//         emit withdrawRewardsEvent(_ownerOfNFT, stockYardBalances, balance);
//     }


//     // Get Contract Info
//    function getBalance() public view returns (uint256){
//         uint256 _balance = address(this).balance;
//         return _balance;
//     }

//     function checkTokenBalance(address _token) external view returns(uint) {
//         IERC20 token = IERC20(_token);
//         return token.balanceOf(address(this));
//     }

//     function getUserRewardBalanceForStockYard(uint _stockYardNumber, address _ownerOfNFT) public view returns (uint256) {
//         if (stockYardRewardBalancesNftOwners[_stockYardNumber][_ownerOfNFT] <= 0){
//             return 0;
//         }
//         return stockYardRewardBalancesNftOwners[_stockYardNumber][_ownerOfNFT];
//     }


//     function getStockYardRewardBalancesForWalletAddress(address _ownerOfNFT) public view returns (uint256[] memory)  {
//         // Determine how many stockyards we should loop over
//         uint stockYardsToCheck = getActiveStockYardCount();
//         uint256[] memory stockYardRewardBalances = new uint256[](stockYardsToCheck);
//         // Loop over stockyards and append to stockYardRewardBalances
//         for (uint i = 0; i < stockYardsToCheck; i++) {
//             stockYardRewardBalances[i] = stockYardRewardBalancesNftOwners[i + 1][_ownerOfNFT];
//         }
//         return stockYardRewardBalances; 
//     }

//     function getTotalStockYardRewardBalanceForWalletAddress(address _ownerOfNFT) public view returns (uint256)  {
//         // Determine how many stockyards we should loop over
//         uint stockYardsToCheck = getActiveStockYardCount();
//         uint256 totalRewards; 
//         // Loop over stockyards and add up all the stockYardRewardBalances for each stockYard
//         for (uint i; i < stockYardsToCheck; i++) {
//             totalRewards += stockYardRewardBalancesNftOwners[i + 1][_ownerOfNFT];
//         }
//         return totalRewards; 
//     }



//     // Minting contract info
//     function getMintTotalSupply() public view returns (uint256) {
//         TheRanchBullsMint TRBM = TheRanchBullsMint(TheRanchBullsMintAddress);
//         return TRBM.totalSupply();
//     }

//     function getNFTOwnerOf(uint _index) public view returns (address) {
//         TheRanchBullsMint TRBM = TheRanchBullsMint(TheRanchBullsMintAddress);
//         return TRBM.ownerOf(_index);
//     }

//     function getWalletOfOwner(address _owner) public view returns (uint256[] memory) {
//         TheRanchBullsMint TRBM = TheRanchBullsMint(TheRanchBullsMintAddress);
//         return TRBM.walletOfOwner(_owner);
//     }

//     function getActiveStockYardCount() public view returns (uint) {
//         TheRanchBullsMint TRBM = TheRanchBullsMint(TheRanchBullsMintAddress);
//         return TRBM.activeStockYardCount();
//     }

//     function getStockYardSize() public view returns (uint) {
//         TheRanchBullsMint TRBM = TheRanchBullsMint(TheRanchBullsMintAddress);
//         return TRBM.stockYardSize();
//     }



//     // Contract Control _ OnlyOwner
//     function setRewardTokenAddress(address _address) public onlyOwner {
//         require(address(_address) != address(0));
//         rewardTokenContract = _address;
//     }

//     function setRewardTokenDecimals(uint _decimals) public onlyOwner {
//         rewardDecimals = _decimals;
//     }

//     function setTheRanchBullsMintAddress(address _mintAddress) public onlyOwner {
//         require(address(_mintAddress) != address(0));
//         TheRanchBullsMintAddress = _mintAddress;
//     }

//     function setWalletAddressForStockYard(uint _stockYard, address _walletAddress) public onlyOwner {
//         require(address(_walletAddress) != address(0));
//         approvedStockYardWalletAddresses[_stockYard] = _walletAddress;
//     }


//     function setcoreTeam1(address payable _address) external  onlyOwner {
//         require(address(_address) != address(0), "ERROR: address can't be address(0)");
//         coreteam_1 = _address;
//     }

//     function setcoreTeam2(address payable _address) external onlyOwner {
//         require(address(_address) != address(0), "ERROR: address can't be address(0)");
//         coreteam_2 = _address;
//     }

//     function setcoreTeam1_percent(uint256 _percent) external onlyOwner {
//         require(coreteam_2_percent + _percent <= 10, "Coreteam1 and Coreteam2 must be 10% or lower");
//         coreteam_1_percent  = _percent;
//     }

//     function setcoreTeam2_percent(uint256 _percent) external onlyOwner {
//         require(coreteam_1_percent + _percent <= 10, "Coreteam1 and Coreteam2 must be 10% or lower");
//         coreteam_2_percent  = _percent;
//     }




// }

