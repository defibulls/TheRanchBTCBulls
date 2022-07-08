// // SPDX-License-Identifier: MIT
// pragma solidity 0.8.7;

// /*    
// 🅣🅗🅔🅡🅐🅝🅒🅗_🅑🅤🅛🅛🅢_➋⓿➋➋
// */


// import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
// import "@chainlink/contracts/src/v0.8/interfaces/VRFCoordinatorV2Interface.sol";
// import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol";
// import "@chainlink/contracts/src/v0.8/interfaces/KeeperCompatibleInterface.sol";
// import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
// import "@openzeppelin/contracts/access/Ownable.sol";
// import "@openzeppelin/contracts/utils/Counters.sol";
// import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
// import "@openzeppelin/contracts/token/ERC20/IERC20.sol";


// import { IERC2981, IERC165 } from "@openzeppelin/contracts/interfaces/IERC2981.sol";


// error Raffle__UpkeepNotNeeded (uint256 USDCRewardsForAddress, uint256 numPlayers, uint256 raffleMintState);
// error Raffle__RaffleIsProcessing();
// error Minting_ExceedsTotalBulls();
// error Minting_ExceedsMintsPerTx();
// error Minting_CantMintZero();
// error Minting_PublicSaleNotLive();
// error Contract_ContractPaused_CheckSocials();

// contract TheRanchBullsMintAndReward is 
//     VRFConsumerBaseV2,
//     KeeperCompatibleInterface,
//     ERC721Enumerable,
//     IERC2981,
//     Ownable,
//     ReentrancyGuard {
    
//     using Strings for uint256;
//     using SafeERC20 for IERC20;
//     using Counters for Counters.Counter;
//     Counters.Counter private _tokenSupply;

//     address public wbtcTokenContract;
//     uint public wbtcTokenDecimals = 8;
//     address public usdcTokenContract;
//     uint public usdcTokenDecimals = 6;

//     // coreTeam Addresses
//     address public coreTeam_1;
//     address public coreTeam_2;
//     uint256 public coreTeam_1_percent = 8;
//     uint256 public coreTeam_2_percent = 2;

//     // Minting 
//     uint256 public mintingCost = 350;  // USDC.e
//     uint public bulls_in_existence = 10000;

//     bool public publicSaleLive = false;
//     bool public paused = true;

//     mapping(address => bool) public isBlacklisted;

//     mapping(address => uint) public userMintCount;  // How many bulls did an address mint
//     mapping(address => bool) public userInDailyRaffle;  // Is the person already in the daily raffle?

//     mapping(address => address) public myPartner;   // partner mapping; msg.sender  ==> who referred them
//     mapping(address => uint256) public myParnterNetworkTeam;   // partner mapping; msg.sender  ==> who referred them

   
   
//      // Contract Balances
//     uint256 public btcMinersBalanceTotal;
//     uint256 public warChestBalance;     // reserve kept for hosting fees and will be used if people don't pay their maintenance fees on time
//     uint256 public USDCRewardsBalanceTotal;    // amount held within contract for referrals and raffle balance 
//     uint256 public dailyRaffleBalance;    // Strictly the Raffle amount of USDC to be award on the raffle 
//     mapping (address => uint256) USDCRewardsForAddress; // amount of USDC user is allowed to via the referral and raffle reward system
//     mapping (address => uint256) WBTCRewardsForAddress;     
  

//     // NFT INFO 
//     string private _tokenBaseURI;
//     string private baseURI;
//     string private baseExtension = ".json";
 
//     // Chainlink VRF Variables
//     VRFCoordinatorV2Interface private  vrfCoordinator;
//     uint64 private subscriptionId;
//     bytes32 private gasLane;
//     uint32 private callbackGasLimit;
//     uint16 private constant REQUEST_CONFIRMATIONS = 3;
//     uint32 private constant NUM_WORDS_DAILY = 1;          // used for daily raffle
  

//     // Raffle Variables
//     uint256 public interval = 86400;
//     uint256 private lastTimeStamp;
//     address[] private dailyRafflePlayers;
//     RaffleMintState private raffleMintState;

//     // Maintenance Fees Variables and Mappings

//     // The amount calculated for hosting invoice / NFT count 
//     uint256 public calculatedMonthlyMaintenanceFee;   


//     // monththy storage that gets reset every month
//     mapping(address => bool) monthlyMaintanenceFeeDue;
//     mapping(address => uint) nftsHeldByAddressAtMonthlyPayout;
//     address[] public addressesToPayMaintenanceFees; 
 
//     // lifetimeStorage
//     mapping(address =>bool) hasAddressEverBeenRewarded;
//     address[] public allAddressThatHaveEverBeenRewarded; 

//     mapping(address => uint256) public totalMaintanenceFeesDue;
//     mapping(address => uint)  public monthsBehindMaintenanceFeeDueDate;


//     /**
//      * @dev This mapping will serve the feeding contract and potenitally more in the future. These contracts will have the ability to call the updateUSDCBonusAmtForAddress
//      * function. As this is the primary reward token for minting and paying Maint Fees, We plan to launch another NFT that will award 
//      * owners on this contract with USDC. The hope being the other project helps each owner of the BTC bulls payoff their maint fees and hopefully more 
//      * to be an additional source of revenue for each Bull Owner 
//     */
//     mapping (address => bool) isAllowedToInteract; 

    

//     /**
//      * @dev For addresses that are more than 3 months behind on the maintenance fees, each 
//      * each address added here will get luquidated
//     */
//     address[] public upForLiquidation; 


//     enum RaffleMintState {
//         OPEN,
//         PROCESSING
//     }



//     /* Events */
//     event RequestedRaffleWinner(uint256 indexed requestId);

//     event NewBullsEnteringRanch(
//         address indexed NewbullOwner,
//         bool indexed RaffleEntered,
//         uint256  BullsPurchased,
//         uint256 _NFTCount
//     );

//     event dailyRaffleWinnerEvent(
//         address indexed raffleWinner,
//         uint256  raffleWinAmount

//     );
    

//     event withdrawUSDCRewardsForAddressEvent(
//         address indexed nftOwner,
//         uint256 indexed totalAmountTransferred
//     );

//     event withdrawWbtcRewardsEvent(
//         address indexed nftOwner,
//         uint256 indexed totalAmountTransferred  
//     );

//     event liquidationEvent (
//         address indexed nftOwner,
//         uint256 indexed totalAmountliquidated
//     );


//     event fundAndRewardEvent(
//             uint256 indexed _totalAmountDeposit,
//             uint indexed _startingIndex,
//             uint indexed _endingIndex
//     );

//     event payMaintanenceFeesEvent(
//             address indexed nftOwner,
//             uint256 indexed totalAmountPayedWithCurrentRewards,
//             uint256 indexed totalAmountPayedWithoutCurrentRewards
//     );



//     constructor(
//         string memory _initBaseURI,
//         address _vrfCoordinatorV2,
//         bytes32 _gasLane, // keyHash
//         uint64 _subscriptionId,
//         uint32 _callbackGasLimit
//     ) 
//         VRFConsumerBaseV2(_vrfCoordinatorV2)
//         ERC721("TheRanch_BTC_BULLS", "TRBB") {

//         setBaseURI(_initBaseURI);  
//         vrfCoordinator = VRFCoordinatorV2Interface(_vrfCoordinatorV2);
//         gasLane = _gasLane;
//         subscriptionId = _subscriptionId;
//         raffleMintState = RaffleMintState.OPEN;
//         lastTimeStamp = block.timestamp;
//         callbackGasLimit = _callbackGasLimit;
//     }


//    // MINTING
//     /**
//      * @dev This is the function does the following things:
//      * 0. Only works if the raffle is NOT PROCESSING, This only happens once a day for a small amount of time. 
//      * 1. Allows users to mint new NFTs 1 - 10 per tx 
//      * 2. Updates Mapping for their total count of mints
//      * 3. Uses a referral/partners system to see who gets the referral bonus.
//      * 4. Enters user into the daily raffle if they chose to do so. 
//      * 5. If msg.sender elects to enter raffle, 95% goes to btcMinersFund, if they do not, 98% does. 
//     */
//     function mint(uint256 _tokenQuantity, bool _enterRaffle) public payable {

//         if (raffleMintState == RaffleMintState.PROCESSING) {revert Raffle__RaffleIsProcessing();}
//         if (paused) { revert Contract_ContractPaused_CheckSocials();}
//         if (!publicSaleLive) { revert Minting_PublicSaleNotLive();}
//         if (_tokenQuantity ==  0) { revert Minting_CantMintZero();}
//         if (_tokenQuantity > 100) {revert Minting_ExceedsMintsPerTx();}
//         if (_tokenSupply.current() + _tokenQuantity > bulls_in_existence) {revert Minting_ExceedsTotalBulls();}


//         IERC20 mintingToken = IERC20(usdcTokenContract);
//         uint256 minting_cost_per_bull = mintingCost * 10 ** usdcTokenDecimals;
    
//         uint256 totalTransactionCost = minting_cost_per_bull * _tokenQuantity;
//         //require(msg.value == totalTransactionCost, "msg.value not equal to total minting transaction cost.");
//         mintingToken.safeTransferFrom(msg.sender, address(this), (totalTransactionCost));

//         for(uint256 i = 0; i < _tokenQuantity; i++) {
//             _tokenSupply.increment();
//             _safeMint(msg.sender, _tokenSupply.current());
//         }

//         //update the mint count for msg.sender
//         userMintCount[msg.sender] += _tokenQuantity;

//         // Voluntary Raffle entry allow users to enter raffle is they choose too with _enterRaffle == True
//         uint256 raffleFundAmt; 

//         if (_enterRaffle == true){
//             raffleFundAmt = totalTransactionCost * 3 / 100;
//             if (getUserAlreadyInDailyRaffleStatus(msg.sender) == false){
//                 dailyRafflePlayers.push(payable(msg.sender));
//                 userInDailyRaffle[msg.sender] = true; 
//             }
//             dailyRaffleBalance += raffleFundAmt;
//         } else {
//             raffleFundAmt = 0;
//         }

//         // update contract balances
//         uint256 referralFundAmt = totalTransactionCost * 2 / 100;
//         uint256 warChestAmt = totalTransactionCost * 5 / 100;
//         uint256 btcMinersFundAmt = totalTransactionCost - (referralFundAmt + raffleFundAmt)  - warChestAmt; 
//         USDCRewardsBalanceTotal += (referralFundAmt + raffleFundAmt);
//         btcMinersBalanceTotal += btcMinersFundAmt;
//         warChestBalance += warChestAmt; 
        
//         // update USDC Reward Balances for referrals
//         address referrer = myPartner[msg.sender];
//         if(referrer != address(0) && userMintCount[referrer] > 0){
//             updateUsdcBonus(referrer, referralFundAmt);
//         }
//         else
//         {
//             uint256 splitReferralAmt = referralFundAmt * 50 / 100;
//             updateUsdcBonus(coreTeam_1, splitReferralAmt);
//             updateUsdcBonus(coreTeam_2, splitReferralAmt);
//         }
        
//         emit NewBullsEnteringRanch(msg.sender,_enterRaffle, _tokenQuantity, _tokenSupply.current());
//     }



//     function fundAndRewardBulls(uint _startingIndex, uint _endingIndex, uint256 _totalAmountToDeposit) public payable onlyOwner {
//         require(paused, "ERROR: Contract must be paused to start the monthly rewarding process");
//         require(_startingIndex < _endingIndex,"ERROR: Start must be lower");
//         require(_startingIndex > 0,"ERROR: Index 0 doesn't exist");
//         require(_endingIndex <= _tokenSupply.current(),"ERROR: This touches an non existent NFT ID");
       
//         // Transfer rewardTokens to the contract
//         IERC20 tokenContract = IERC20(wbtcTokenContract);
//         tokenContract.safeTransferFrom(msg.sender, address(this), _totalAmountToDeposit);

//         // store the 10% Core team values to send later in the function
//         uint256 coreTeam_1_amt; 
//         uint256 coreTeam_2_amt; 
    

//         coreTeam_1_amt += _totalAmountToDeposit * coreTeam_1_percent / 100;
//         coreTeam_2_amt += _totalAmountToDeposit * coreTeam_2_percent / 100;

//         uint256 _disperableAmount = (_totalAmountToDeposit * (100 - (coreTeam_1_percent + coreTeam_2_percent)) / 100); 

//         uint256 payout_per_nft = _disperableAmount / ((_endingIndex - _startingIndex) + 1);
        
//         for( uint i = _startingIndex; i <= _endingIndex; i++) {
//             address bullOwner = ownerOf(i);
//             if (bullOwner != address(0)){

//                 if (monthlyMaintanenceFeeDue[bullOwner] == false){
//                     monthlyMaintanenceFeeDue[bullOwner] = true;
//                     addressesToPayMaintenanceFees.push(bullOwner);
//                 }

//                 nftsHeldByAddressAtMonthlyPayout[bullOwner] += 1;


//                 address referrer = myPartner[bullOwner];
//                 uint256 referralAmt = payout_per_nft * 1 / 100;
                
//                 if(referrer != address(0) && userMintCount[referrer] > 0){
//                     updateWBTCRewardBalanceForAddress(referrer, referralAmt);
//                     updateWBTCRewardBalanceForAddress(bullOwner, (payout_per_nft - referralAmt));
//                 } else {
//                     updateWBTCRewardBalanceForAddress(coreTeam_1, referralAmt);
//                     updateWBTCRewardBalanceForAddress(coreTeam_2, referralAmt);
//                     updateWBTCRewardBalanceForAddress(bullOwner, (payout_per_nft - (referralAmt * 2)));
//                 }
//             }
//         }


//         updateWBTCRewardBalanceForAddress(coreTeam_1, coreTeam_1_amt);
//         updateWBTCRewardBalanceForAddress(coreTeam_2, coreTeam_2_amt);
//         emit fundAndRewardEvent(_totalAmountToDeposit, _startingIndex, _endingIndex);

//     }

//     /**
//     * @dev When The Feeding Contract checks the owners of the NFTs (HayBales NFTs) from that contract, it reaches 
//     * over to this contract and tries to update the USDC amount within these rules:
//     * if the HayBale owner also owns a Bull NFT on this contract, they'll get 100% of the paycut.
//     * if the Haybale owner does not own a bull, they will share the paycut 50/50 with CoreTeam_1 
//     */
//     function updateUsdcBonusFromAnotherContract(address _ownerOfNFT, uint256 _amountToAdd) external {
//         require(isAllowedToInteract[msg.sender] == true, "You are not allowed to call this function");

//         if (balanceOf(_ownerOfNFT) > 0){
//             USDCRewardsForAddress[_ownerOfNFT] += _amountToAdd;
//         } else {
//             uint256 splitBonusAmt = _amountToAdd * 50 / 100;
//             USDCRewardsForAddress[_ownerOfNFT] += splitBonusAmt;
//             USDCRewardsForAddress[coreTeam_1] += splitBonusAmt;
//         }
//     }

//     function updateMaintenanceFeesForTheMonth() external onlyOwner {
//         require(paused, "ERROR: Contract must be paused to start the monthly rewarding process");
//         require(calculatedMonthlyMaintenanceFee != 0, "You must set the Calculated Monthly Maintenance Fee First");
//         require(addressesToPayMaintenanceFees.length > 0, "Must fund and award first");


//         address[] memory _addressesToPayMaintenanceFees = addressesToPayMaintenanceFees; 


//         for( uint i; i < _addressesToPayMaintenanceFees.length; i++) {
//             address _ownerOfNFTs = _addressesToPayMaintenanceFees[i];
//             uint _nftCount = nftsHeldByAddressAtMonthlyPayout[_ownerOfNFTs];


//             if (hasAddressEverBeenRewarded[_ownerOfNFTs] == false){
//                 // update that they have been rewarded before
//                 hasAddressEverBeenRewarded[_ownerOfNFTs] = true;
//                 allAddressThatHaveEverBeenRewarded.push(_ownerOfNFTs);
//             }
//             // update the amount the user owes in maintenance fees because they were rewarded this month.
//             totalMaintanenceFeesDue[_ownerOfNFTs] += _nftCount * calculatedMonthlyMaintenanceFee;

//             // reset the monthly mapping so they'll be added next month if rewarded again. 
//             monthlyMaintanenceFeeDue[_ownerOfNFTs] = false;
//             nftsHeldByAddressAtMonthlyPayout[_ownerOfNFTs] = 0;
//         }

//         // reset calculatedMonthlyMaintenanceFee and addresses found to pay them
//         calculatedMonthlyMaintenanceFee = 0;
//         addressesToPayMaintenanceFees = new address[](0);
//     }


//     function updateMonthsBehindMaintenanceFeeDueDate() external onlyOwner {
//         require(paused, "ERROR: Contract must be paused to start the monthly rewarding process");

//         address[] memory _allAddressThatHaveEverBeenRewarded = allAddressThatHaveEverBeenRewarded; 


//         for( uint i; i < _allAddressThatHaveEverBeenRewarded.length; i++) {
//             address _address = _allAddressThatHaveEverBeenRewarded[i];
//             if (totalMaintanenceFeesDue[_address] > 0) {
//                 monthsBehindMaintenanceFeeDueDate[_address] += 1;
//             }

//             // If an _address is more than 3 months behind on maintenance Fees, they will get liquidated
//             if (monthsBehindMaintenanceFeeDueDate[_address] == 4){
//                 upForLiquidation.push(_address);
//             }
//         }
//     }


//     function getLiquidatedArray() public view returns ( address [] memory) {
//         return upForLiquidation;
//     }


//     function liquidateOutstandingAccounts() external onlyOwner {
//         require(paused, "ERROR: Contract must be paused to start the monthly rewarding process");
//         require(upForLiquidation.length > 0, "No one meets liquidation criteria.");
//         for( uint i; i < upForLiquidation.length; i++) {
//             address _culprit = upForLiquidation[i];
//             uint256 _amount = WBTCRewardsForAddress[_culprit];
//             WBTCRewardsForAddress[_culprit] = 0;
//             WBTCRewardsForAddress[coreTeam_1] = _amount;

//             // reset fees and months behind. 
//             totalMaintanenceFeesDue[_culprit] = 0;
//             monthsBehindMaintenanceFeeDueDate[_culprit] = 0;
//             emit liquidationEvent(_culprit, _amount) ;
            
//         }
//         upForLiquidation = new address[](0);
//     }


//     /**
//      * @dev If the user has USDC rewards to claim
//      * the maintanence fee balance will be deducted from that. 
//      * If it doesn't cover the entire maintenance fee cost, 
//      * the rest of the amount will be asked to approved and sent to the contract. 
//     **/
//     function payMaintanenceFees() external nonReentrant {
//         uint256 _balance = USDCRewardsForAddress[msg.sender];
//         uint256 _feesDue = totalMaintanenceFeesDue[msg.sender];

//         if (_balance >= _feesDue){

//             USDCRewardsForAddress[msg.sender] -= _feesDue; 
//             USDCRewardsForAddress[coreTeam_1] += _feesDue; 

//             emit payMaintanenceFeesEvent(msg.sender, _feesDue, 0);
//         } else {

//             IERC20 mintingToken = IERC20(usdcTokenContract);

//             uint256 amt_needed =  _feesDue - _balance;
//             mintingToken.safeTransferFrom(msg.sender, address(this), (amt_needed));
//             USDCRewardsForAddress[coreTeam_1] += amt_needed; 

//             if (_balance > 0){
//                 USDCRewardsForAddress[msg.sender] -= _balance; 
//                 USDCRewardsForAddress[coreTeam_1] += _balance; 
//             }

//             emit payMaintanenceFeesEvent(msg.sender, _balance, amt_needed);
//         }

//         // reset fees and months behind. 
//         totalMaintanenceFeesDue[msg.sender] = 0;
//         monthsBehindMaintenanceFeeDueDate[msg.sender] = 0;

//     }




//     function updateWBTCRewardBalanceForAddress(address _ownerOfNFT, uint256 _amount) internal {
//         WBTCRewardsForAddress[_ownerOfNFT] +=  _amount;
//     }

//     function getWbtcRewardBalanceForAddress() public view returns (uint256) {
//         return WBTCRewardsForAddress[msg.sender]; 
//     }

//     // Chainlink Integration 
//      /**
//      * @dev This is the function that the Chainlink Keeper nodes call
//      * they look for `upkeepNeeded` to return True.
//      * the following should be true for this to return true:
//      * 1. The time interval has passed between raffle runs.
//      * 2. The raffle is open.
//      * 3. The USDCRewardsForAddress is greater than 0.
//      * 4. Implicity, chainlink subscription is funded with LINK.
//      */
//     function checkUpkeep(
//         bytes memory /* checkData */
//     )
//         public
//         view
//         override
//         returns (
//             bool upkeepNeeded,
//             bytes memory /* performData */
//         )
//     {
//         bool isOpen = RaffleMintState.OPEN == raffleMintState;
//         bool timePassed = ((block.timestamp - lastTimeStamp) > interval);
//         bool hasPlayers = dailyRafflePlayers.length > 0;
//         bool hasBalance = USDCRewardsBalanceTotal > 0;
//         upkeepNeeded = (timePassed && isOpen && hasBalance && hasPlayers);
//         return (upkeepNeeded, "0x0"); 
//     }




//     /**
//      * @dev Once `checkUpkeep` is returning `true`, this function is called
//      * and it kicks off a Chainlink VRF call to get a random winner.
//      */
//     function performUpkeep(
//         bytes calldata /* performData */
//     ) external override {
//         (bool upkeepNeeded, ) = checkUpkeep("");
//         // require(upkeepNeeded, "Upkeep not needed");
//         if (!upkeepNeeded) {
//             revert Raffle__UpkeepNotNeeded(
//                 USDCRewardsBalanceTotal,
//                 dailyRafflePlayers.length,
//                 uint256(raffleMintState)
//             );
//         }
//         raffleMintState = RaffleMintState.PROCESSING;
//         uint256 requestId = vrfCoordinator.requestRandomWords(
//             gasLane,
//             subscriptionId,
//             REQUEST_CONFIRMATIONS,
//             callbackGasLimit,
//             NUM_WORDS_DAILY
//         );
//         emit RequestedRaffleWinner(requestId);
//     }


//     /**
//      * @dev This is the function that Chainlink VRF node
//      * calls to send the money to the random winner.
//      */
//     function fulfillRandomWords(
//         uint256, /* requestId */
//         uint256[] memory randomWords
//     ) internal override {
     
//         // DAILY RAFFLE SECTION // 
//         uint256 indexOfWinner = randomWords[0] % dailyRafflePlayers.length;
//         address dailYRaffleWinner = dailyRafflePlayers[indexOfWinner];
//         uint256 raffleWinningAmount = dailyRaffleBalance; 

//         // update the daily raffle winnner balance on reward contract
//         updateUsdcBonus(dailYRaffleWinner, dailyRaffleBalance);

//         resetUserInDailyRaffle(); // must do before resetting dailyRafflePlayers
//         dailyRaffleBalance = 0;  // reset dailyRaffleBalance back to zero after drawing
//         dailyRafflePlayers = new address[](0);

//         lastTimeStamp = block.timestamp;
//         raffleMintState = RaffleMintState.OPEN;
//         emit dailyRaffleWinnerEvent(dailYRaffleWinner, raffleWinningAmount);

//     }
    

//     /**
//      * @dev Once the raffle winner is picked, we loop through the dailyRafflePlayers
//      * and set their booling value back to false so they can enter another raffle 
//      * if they choose to mint more NFTs later.
//      */
//     function resetUserInDailyRaffle() internal {
//         for (uint i=0; i< dailyRafflePlayers.length ; i++){
//             userInDailyRaffle[dailyRafflePlayers[i]] = false;
//         }
//     }


//     function setPartnerAddress(address _newPartner)  public {
//         require(address(_newPartner) != address(0), "ERROR: address can't be address(0)");
//         require(address(_newPartner) != msg.sender, "ERROR: address can't be yourself");

//         address currentPartner = myPartner[msg.sender];
//         // myPartner[msg.sender] = _newPartner;

//         if (currentPartner == address(0)){
//             myPartner[msg.sender] = _newPartner;
//             myParnterNetworkTeam[_newPartner] += 1;
//         } else {
//             myPartner[msg.sender] = _newPartner;
//             myParnterNetworkTeam[currentPartner] -= 1;
//             myParnterNetworkTeam[_newPartner] += 1;
//         }
//     }

//     // Contract Funding / Withdrawing / Transferring
//     function fund() public payable {}

//     function withdraw() external onlyOwner {
//         payable(owner()).transfer(address(this).balance);
//     }

//     function withdrawToken(address _tokenContract, uint256 _amount) external onlyOwner {
//         IERC20 tokenContract = IERC20(_tokenContract);
//         tokenContract.safeTransfer(msg.sender, _amount);
//     }

//     function withdrawBtcMinerBalance() external onlyOwner {
//         IERC20 tokenContract = IERC20(usdcTokenContract);
//         uint256 amtToTransfer = btcMinersBalanceTotal; 
//         tokenContract.safeTransfer(msg.sender, amtToTransfer);
//         btcMinersBalanceTotal -= amtToTransfer;
//     }

//     function withdrawWarChestBalance() external onlyOwner {
//         IERC20 tokenContract = IERC20(usdcTokenContract);
//         uint256 amtToTransfer = warChestBalance; 
//         tokenContract.safeTransfer(msg.sender, amtToTransfer);
//         warChestBalance -= amtToTransfer;
//     }


//     function withdrawWbtcForWalletAddress() external nonReentrant {
//         require(!paused, "ERROR: Contract Paused. Please Check Discord.");
//         require(!isBlacklisted[msg.sender], "Blacklisted address");
//         require(totalMaintanenceFeesDue[msg.sender] == 0, "You must pay all maintenance fees before WBTC withdrawal is allowed");

//         // Get the total Balance to award the owner of the NFT(s)
//         uint256 myBalance = WBTCRewardsForAddress[msg.sender];
//         require(myBalance > 0, "You must have a balance more than 0");
  
//         // Transfer Balance 
//         IERC20(wbtcTokenContract).safeTransfer(msg.sender, myBalance );

//         // update wbtc balance for nft owner
//         WBTCRewardsForAddress[msg.sender] = 0;
        
//         emit withdrawWbtcRewardsEvent(msg.sender, myBalance);

//     }

//     function withdrawUsdcRewardBalance() external nonReentrant {

//         require(!paused, "ERROR: Contract Paused. Please Check Discord.");
//         require(!isBlacklisted[msg.sender], "Blacklisted address");
        
//         // Get USDC rewards balance for msg.sender
//         uint256 myBalance = USDCRewardsForAddress[msg.sender];
//         require(myBalance > 0, "You must have a balance more than 0");
 

//         // Transfer Balance 
//         IERC20(usdcTokenContract).safeTransfer(msg.sender, (myBalance));
//         // update mapping on contract 
//         USDCRewardsForAddress[msg.sender] = 0;
//         // update USDC Rewards Balance Total
//         USDCRewardsBalanceTotal -= myBalance;
        
//         // emit event
//         emit withdrawUSDCRewardsForAddressEvent(msg.sender, myBalance);
        
//     }

//     function updateUsdcBonus(address _recipient, uint256 _amountToAdd) internal {
//         USDCRewardsForAddress[_recipient] += _amountToAdd;
//     }



//     function getUsdcRewardBalanceForAddress() public view returns (uint256) {
//         return USDCRewardsForAddress[msg.sender];
//     }


//     /** Getter Functions */

//     /**
//      * @dev returns how many people are using them as someone as their partner
//      */
//     function getPartnerNetworkTeamCount(address _adressToCheck) public view returns (uint) {
//         return myParnterNetworkTeam[_adressToCheck];
//     }

//     /**
//      * @dev checks if an address is using them as their partner.
//      */
//     function getAreTheyOnMyPartnerNetworkTeam(address _adressToCheck) public view returns (bool) {
//         if (myPartner[_adressToCheck] == msg.sender){
//             return true;
//         }
//         return false;
//     }

//     /**
//     * @dev checks if an address is using you as their partner.
//     */
//     function getHaveTheyMintedBefore(address _adressToCheck) public view returns (bool) {
//         if (userMintCount[_adressToCheck] > 0){
//             return true;
//         }
//         return false;
//     }

   
//     function getMintCountForAddress(address _address) public view returns (uint) {
//         return userMintCount[_address];
//     }

//     function getUserAlreadyInDailyRaffleStatus(address _address) public view returns (bool) {
//         return userInDailyRaffle[_address];
//     }

//     function walletOfOwner(address _owner) public view returns (uint256[] memory) {
//         uint256 ownerTokenCount = balanceOf(_owner);
//         uint256[] memory tokenIds = new uint256[](ownerTokenCount);
//         for (uint256 i; i < ownerTokenCount; i++) {
//             tokenIds[i] = tokenOfOwnerByIndex(_owner, i);
//         }
//         return tokenIds;
//     }

//     function getRaffleMintState() public view returns (RaffleMintState) {
//         return raffleMintState;
//     }

 
//     function getRequestConfirmations() public pure returns (uint256) {
//         return REQUEST_CONFIRMATIONS;
//     }


//     function getRafflePlayer(uint256 index) public view returns (address) {
//         return dailyRafflePlayers[index];
//     }

//     function getLastTimeStamp() public view returns (uint256) {
//         return lastTimeStamp;
//     }

//     function getRaffleInterval() public view returns (uint256) {
//         return interval;
//     }

//     function getNumberOfRafflePlayers() public view returns (uint256) {
//         return dailyRafflePlayers.length;
//     }   

//     function getBlacklistedStatus(address _address) public view returns (bool) {
//         return isBlacklisted[_address];
//     }

 

//    // METADATA
//     function _baseURI() internal view virtual override returns (string memory) {
//         return baseURI;
//     }

//     function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
//         require(_exists(tokenId),"ERC721Metadata: URI query for nonexistent token");
//         string memory currentBaseURI = _baseURI();
//         return bytes(currentBaseURI).length > 0 ? string(abi.encodePacked(currentBaseURI, tokenId.toString(), baseExtension)) : "";
//     }

//     // ERC165
//     function supportsInterface(bytes4 interfaceId) public view override(ERC721Enumerable, IERC165) returns (bool) {
//         return interfaceId == type(IERC2981).interfaceId || super.supportsInterface(interfaceId);
//     }

//     // IERC2981
//     function royaltyInfo(uint256 _tokenId, uint256 _salePrice) external view override returns (address, uint256 royaltyAmount) {
//         _tokenId; // silence solc warning
//         royaltyAmount = _salePrice * 10 / 100;  // 10%
//         return (coreTeam_1, royaltyAmount);
//     }


//     // Contract Control _ OnlyOwner
//     function setBaseURI(string memory _newBaseURI) public onlyOwner {
//             baseURI = _newBaseURI;
//     }


//     function setBaseExtension(string memory _newBaseExtension) external onlyOwner {
//             baseExtension = _newBaseExtension;
//     }

//     function togglePublicSaleStatus() external onlyOwner {
//         publicSaleLive = !publicSaleLive;
//     }

//     function togglePauseStatus() external onlyOwner {
//         require(address(coreTeam_1) != address(0), "ERROR: The coreTeam_1 address must be set prior to any minting");
//         require(address(coreTeam_2) != address(0), "ERROR: The coreTeam_2 address must be set prior to any minting");
//         require(address(usdcTokenContract) != address(0), "ERROR: The usdcTokenContract address must be set prior to any minting");
//         require(address(wbtcTokenContract) != address(0), "ERROR: The wbtcTokenContract address must be set prior to any minting");
//         paused = !paused;
//     }

//     function setCoreTeam_1_Address(address _coreTeam_1) public onlyOwner {
//         require(address(_coreTeam_1) != address(0), "ERROR: The coreTeam_1 address can't be address(0)");
//         coreTeam_1 = _coreTeam_1;
//     }

//     function setCoreTeam_2_Address(address _coreTeam_2) public onlyOwner {
//         require(address(_coreTeam_2) != address(0), "ERROR: The coreTeam_2 address can't be address(0)");
//         coreTeam_2 = _coreTeam_2;
//     }

//     function setCoreTeam_1_Percent(uint256 _percent) external onlyOwner {
//         require(coreTeam_2_percent + _percent <= 10, "coreTeam_1 and coreTeam_2 must be 10% or lower");
//         coreTeam_1_percent  = _percent;
//     }

//     function setCoreTeam_2_Percent(uint256 _percent) external onlyOwner {
//         require(coreTeam_1_percent + _percent <= 10, "coreTeam_1 and coreTeam_2 must be 10% or lower");
//         coreTeam_2_percent  = _percent;
//     }

//     function set_minting_price(uint _price) external onlyOwner {
//         require(paused, "ERROR: CANT CHANGE PRICE IF CONTRACT IS NOT PAUSED");
//         mintingCost = _price;
//     }

//     function setUsdcTokenAddress(address _address) public onlyOwner {
//         require(address(_address ) != address(0), "ERROR: The Minting address can't be address(0)");
//         usdcTokenContract = _address;
//     }

//     function setUsdcTokenDecimals(uint _decimals) public onlyOwner {
//         usdcTokenDecimals = _decimals;
//     }

//     function setWbtcTokenAddress(address _address) public onlyOwner {
//         require(address(_address ) != address(0), "ERROR: The Minting address can't be address(0)");
//         wbtcTokenContract = _address;
//     }

//     function setWbtcTokenDecimals(uint _decimals) public onlyOwner {
//         wbtcTokenDecimals = _decimals;
//     }

//     function setSubscriptionId(uint64 _subscriptionId) public onlyOwner {
//         subscriptionId = _subscriptionId;
//     }

//     function setGasLane(bytes32 _gasLane) public onlyOwner {
//         gasLane = _gasLane;
//     }

//     function setCallbackGasLimit(uint32 _callbackGasLimit) public onlyOwner {
//         callbackGasLimit = _callbackGasLimit;
//     }

//     function setVrfCoordinator(VRFCoordinatorV2Interface _vrfCoordinator) public onlyOwner {
//         vrfCoordinator = _vrfCoordinator;
//     }

//     function setInterval(uint256 _interval) public onlyOwner {
//         interval = _interval;
//     }


//     function blacklistMalicious(address account, bool value) external onlyOwner {
//         isBlacklisted[account] = value;
//     }

//     function setMonthlyMaintenanceFeePerNFT(uint256 _monthly_maint_fee_per_nft) external onlyOwner {
//         calculatedMonthlyMaintenanceFee = _monthly_maint_fee_per_nft;
//     }

//     function setAllowedContractsToAwardTheBulls(address _address, bool _bool) public onlyOwner {
//         require( _address != address(0), "Can't be address(0)");
//         isAllowedToInteract[_address] = _bool;
//     }



// }


