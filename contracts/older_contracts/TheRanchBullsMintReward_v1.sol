// // SPDX-License-Identifier: MIT
// pragma solidity 0.8.7;

// /*    
// 🅣🅗🅔🅡🅐🅝🅒🅗_🅑🅤🅛🅛🅢_➋⓿➋➋
// */


// import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
// import "@chainlink/contracts/src/v0.8/interfaces/VRFCoordinatorV2Interface.sol";
// import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol";
// import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
// import "@openzeppelin/contracts/access/AccessControl.sol";
// import "@openzeppelin/contracts/access/Ownable.sol";
// import "@openzeppelin/contracts/utils/Counters.sol";
// import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
// import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
// import { IERC2981, IERC165 } from "@openzeppelin/contracts/interfaces/IERC2981.sol";


// error Minting_ExceedsTotalBulls();
// error Minting_PublicSaleNotLive();
// error Minting_IsZeroOrBiggerThanTen();
// error Contract_CurrentlyPaused_CheckSocials();
// error Pause_MustSetAllVariablesFirst();
// error Pause_BaseURIMustBeSetFirst();
// error Pause_MustBePaused();
// error Rewarding_NotReady();
// error Maintenance_UpdatingNotReady();
// error Liquidation_NothingToDo();
// error Stockyard_BadInputParameter();
// error Stockyard_IsNotSetYet();
// error Partner_NotAllowed();
// error Address_CantBeAddressZero();
// error Blacklisted();
// error Rewarding_NoBalanceToWithdraw();

// contract TheRanchBullsMintReward is 
//     VRFConsumerBaseV2,
//     ERC721Enumerable,
//     IERC2981,
//     AccessControl,
//     Ownable,
//     ReentrancyGuard {

   
//     /**
//      * @dev These ECOSYSTEM_ROLE is for other contracts that are allowed to update the USDC for BTC BULL Owners on this contract.
//     */
//     bytes32 public constant ECOSYSTEM_ROLE = keccak256("ECOSYSTEM_ROLE");
//     bytes32 public constant DEFENDER_ROLE = keccak256("DEFENDER_ROLE");

//     modifier ADMIN_OR_DEFENDER {
//         require(msg.sender == owner() || hasRole(DEFENDER_ROLE, msg.sender), "Caller is not an OWNER OR DEFENDER");
//         _;
//     }

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
//     uint public constant maxSupply = 10000;

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
//     address[] private dailyRafflePlayers;
 
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
//      * @dev For addresses that are more than 3 months behind on the maintenance fees, each 
//      * each address added here will get luquidated
//     */
//     address[] internal upForLiquidation; 

//     // Stockyard allows the rewardBulls function to be more modular. 
//     struct StockyardInfo {
//         uint startingIndex;
//         uint endingIndex;
//         uint256 disperableAmount;
//     }

//     mapping (uint => StockyardInfo) public stockyardInfo;

//     /* Events */
//     event RequestedRaffleWinner(uint256 indexed requestId);

//     event LoadedFundsIntoStockyard(
//         uint stockyardNumber,
//         uint256 indexed amountDeposited,
//         address indexed sender
    
//     );


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


//     event RewardEvent(
//             uint256 totalAmountDispersed,
//             uint256 payPerNFT,
//             uint indexed startingIndex,
//             uint indexed endingIndex
//     );


//     event MaintenanceFeeUpdatingEvent(
//             uint monthlyMaintFee,
//             string sectionMessage
//     );

//     event MaintenanceFeeEvent(
//             string sectionMessage
//     );

//     event payMaintanenceFeesEvent(
//             address indexed nftOwner,
//             uint256 indexed totalAmountPayedWithCurrentRewards,
//             uint256 indexed totalAmountPayedWithoutCurrentRewards
//     );



//     constructor(
//         address _coreTeam_1,
//         address _coreTeam_2,
//         string memory _initBaseURI,
//         address _vrfCoordinatorV2,
//         bytes32 _gasLane, // keyHash
//         uint64 _subscriptionId,
//         uint32 _callbackGasLimit
//     ) 
//         VRFConsumerBaseV2(_vrfCoordinatorV2)
//         ERC721("TheRanch_BTC_BULLS", "TRBB") {



//         if (address(_coreTeam_1) == address(0)) { revert Address_CantBeAddressZero();}
//         if (address(_coreTeam_2) == address(0)) { revert Address_CantBeAddressZero();}
//         coreTeam_1 = _coreTeam_1;
//         coreTeam_2 = _coreTeam_2;

//         _setupRole(DEFAULT_ADMIN_ROLE, owner());
        
//         //setBaseURI(_initBaseURI);  
//         vrfCoordinator = VRFCoordinatorV2Interface(_vrfCoordinatorV2);
//         gasLane = _gasLane;
//         subscriptionId = _subscriptionId;
//         callbackGasLimit = _callbackGasLimit;


//         // // CoreTeam1 member will be in charge of transferring these NFTs to people helping the project such as multisig help, advertisement, security help.
//         // for(uint256 i = 0; i < 15; i++) {
//         //     _tokenSupply.increment();
//         //     _safeMint(_coreTeam_1, _tokenSupply.current());
//         // }

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
//         if (paused) { revert Contract_CurrentlyPaused_CheckSocials();}
//         if (!publicSaleLive) { revert Minting_PublicSaleNotLive();}
//         if (_tokenQuantity ==  0 || _tokenQuantity > 10) { revert Minting_IsZeroOrBiggerThanTen();}
//         // if (_tokenQuantity > 100) {revert Minting_ExceedsMintsPerTx();}
//         if (_tokenSupply.current() + _tokenQuantity > maxSupply) {revert Minting_ExceedsTotalBulls();}


//         IERC20 mintingToken = IERC20(usdcTokenContract);
//         uint256 minting_cost_per_bull = mintingCost * 10 ** usdcTokenDecimals;
//         uint256 totalTransactionCost = minting_cost_per_bull * _tokenQuantity;
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

//     function fundBulls(uint _stockyardNumber, uint256 _totalAmountToDeposit) public payable ADMIN_OR_DEFENDER{
//         // Transfer rewardTokens to the contract
//         if (stockyardInfo[_stockyardNumber].startingIndex == 0) { revert Stockyard_IsNotSetYet();}
//         IERC20 tokenContract = IERC20(wbtcTokenContract);
//         tokenContract.safeTransferFrom(msg.sender, address(this), _totalAmountToDeposit);

//         stockyardInfo[_stockyardNumber].disperableAmount += _totalAmountToDeposit;
//         emit LoadedFundsIntoStockyard(_stockyardNumber,_totalAmountToDeposit, msg.sender);
//     }


//     function rewardBulls(uint _stockyardNumber) public payable ADMIN_OR_DEFENDER {
//         if (calculatedMonthlyMaintenanceFee == 0) { revert Rewarding_NotReady();}
//         if (stockyardInfo[_stockyardNumber].disperableAmount == 0) { revert Rewarding_NotReady();}
//         if (!paused) { revert Pause_MustBePaused();}

        
//         // store the 10% Core team values to send later in the function
//         uint256 coreTeam_1_amt; 
//         uint256 coreTeam_2_amt; 

//         uint startingIndex = stockyardInfo[_stockyardNumber].startingIndex;
//         uint endingIndex = stockyardInfo[_stockyardNumber].endingIndex;

//         uint256 monthlyAmountToDisperse = stockyardInfo[_stockyardNumber].disperableAmount;
    

//         coreTeam_1_amt += monthlyAmountToDisperse * coreTeam_1_percent / 100;
//         coreTeam_2_amt += monthlyAmountToDisperse * coreTeam_2_percent / 100;


//         uint256 _disperableAmount = (monthlyAmountToDisperse * (100 - (coreTeam_1_percent + coreTeam_2_percent)) / 100); 
//         uint256 payout_per_nft = _disperableAmount / ((endingIndex - startingIndex) + 1);


//         for( uint i = startingIndex; i <= endingIndex; i++) {
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
    
//         emit RewardEvent(monthlyAmountToDisperse, payout_per_nft, startingIndex, endingIndex);

//         // reset monthly amount for stockyard
//         stockyardInfo[_stockyardNumber].disperableAmount = 0;
//     }

//     // passing a memory array to do this all in one external call
//     /**
//     * @dev When any other contract in our ecosystem checks the owners of the BTC BullsNFTs, it will updated the USDC amount for the 
//     * BTC Bulls owner on this contract. It incentives ownership of both NFTS this way: 
//     * if the HayBale owner also owns a Bull NFT on this contract, they'll get 100% of the paycut.
//     * if the Haybale owner does not own a bull, they will share the paycut 50/50 with CoreTeam_1 
//     */
//     function updateUsdcBonusFromAnotherContract(address[] memory _ownersOfTheNFTs, uint256 _amountToAdd) external {
//         require(hasRole(ECOSYSTEM_ROLE, msg.sender), "must be approved to interact");

//         for( uint i; i < _ownersOfTheNFTs.length; i++) {
//             address _ownerOfNFT = _ownersOfTheNFTs[i];
//             if (balanceOf(_ownerOfNFT) > 0){
//                 USDCRewardsForAddress[_ownerOfNFT] += _amountToAdd;
//             } else {
//                 uint256 splitBonusAmt = _amountToAdd * 50 / 100;
//                 USDCRewardsForAddress[_ownerOfNFT] += splitBonusAmt;
//                 USDCRewardsForAddress[coreTeam_1] += splitBonusAmt;
//             }
//         }
//     }




//     function updateMaintenanceFeesForTheMonth() external ADMIN_OR_DEFENDER {
//         if (!paused) { revert Maintenance_UpdatingNotReady();}
//         if (addressesToPayMaintenanceFees.length < 1) { revert Pause_MustBePaused();}
        
//         address[] memory _addressesToPayMaintenanceFees = addressesToPayMaintenanceFees; 

//         uint _calculatedMonthlyMaintenanceFee = calculatedMonthlyMaintenanceFee;
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

//         // emit finishing event
//         emit MaintenanceFeeUpdatingEvent(_calculatedMonthlyMaintenanceFee, '_STEP2DONE_ Updated Monthly Fees For Current BTC Bull Owners' );
//     }


//     function updateMonthsBehindMaintenanceFeeDueDate() external ADMIN_OR_DEFENDER{
//         if (!paused) { revert Maintenance_UpdatingNotReady();}

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

//         // emit event
//         emit MaintenanceFeeEvent('_STEP3DONE_ Updated How Many Months Behind For BTC Bull Owners');

//     }


//     function getLiquidatedArrayLength() public view ADMIN_OR_DEFENDER returns (uint) {
//         return upForLiquidation.length;
//     }

//     function liquidateOutstandingAccounts() external ADMIN_OR_DEFENDER {
//         if (!paused) { revert Maintenance_UpdatingNotReady();}
//         if (upForLiquidation.length < 1) { revert Liquidation_NothingToDo();}

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
        
//         // emit event
//         emit MaintenanceFeeEvent('Finished Liquidated Outstanding Accounts');
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


//     function kickOffDailyRaffle() external ADMIN_OR_DEFENDER {
//         paused = !paused;  //Pause contract everytime the raffle happens 
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
//         if (address(_newPartner) == address(0)) { revert Partner_NotAllowed();}
//         if (address(_newPartner) == msg.sender) { revert Partner_NotAllowed();}

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

//     function withdraw() external ADMIN_OR_DEFENDER {
//         payable(msg.sender).transfer(address(this).balance);
//     }

//     function withdrawToken(address _tokenContract, uint256 _amount) external ADMIN_OR_DEFENDER {
//         IERC20 tokenContract = IERC20(_tokenContract);
//         tokenContract.safeTransfer(msg.sender, _amount);
//     }

//     function withdrawBtcMinerBalance() external ADMIN_OR_DEFENDER {
//         IERC20 tokenContract = IERC20(usdcTokenContract);
//         uint256 amtToTransfer = btcMinersBalanceTotal; 
//         tokenContract.safeTransfer(owner(), amtToTransfer);
//         btcMinersBalanceTotal -= amtToTransfer;
//     }

//     function withdrawWarChestBalance() external ADMIN_OR_DEFENDER {
//         IERC20 tokenContract = IERC20(usdcTokenContract);
//         uint256 amtToTransfer = warChestBalance; 
//         tokenContract.safeTransfer(owner(), amtToTransfer);
//         warChestBalance -= amtToTransfer;
//     }

//     function withdrawWbtcForWalletAddress() external nonReentrant {
//         if (paused) { revert Contract_CurrentlyPaused_CheckSocials();}
//         if (isBlacklisted[msg.sender]) { revert Blacklisted();}

//         require(totalMaintanenceFeesDue[msg.sender] == 0, "You must pay maintenance fee balance before WBTC withdrawal is allowed");

//         // Get the total Balance to award the owner of the NFT(s)
//         uint256 myBalance = WBTCRewardsForAddress[msg.sender];
//         if (myBalance == 0) { revert Rewarding_NoBalanceToWithdraw();}

//         // Transfer Balance 
//         IERC20(wbtcTokenContract).safeTransfer(msg.sender, myBalance );

//         // update wbtc balance for nft owner
//         WBTCRewardsForAddress[msg.sender] = 0;
        
//         emit withdrawWbtcRewardsEvent(msg.sender, myBalance);
//     }

//     function withdrawUsdcRewardBalance() external nonReentrant {
//         if (paused) { revert Contract_CurrentlyPaused_CheckSocials();}
//         if (isBlacklisted[msg.sender]) { revert Blacklisted();}
        
//         // Get USDC rewards balance for msg.sender
//         uint256 myBalance = USDCRewardsForAddress[msg.sender];
//         if (myBalance == 0) { revert Rewarding_NoBalanceToWithdraw();}
 
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
//     * @dev checks if an address has minted before on the contract.
//     */
//     function getHaveTheyMintedBefore(address _adressToCheck) external view returns (bool) {
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

//     function getRequestConfirmations() public pure returns (uint256) {
//         return REQUEST_CONFIRMATIONS;
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
//     function supportsInterface(bytes4 interfaceId) public view override(ERC721Enumerable, IERC165, AccessControl) returns (bool) {
//         return interfaceId == type(IERC2981).interfaceId || super.supportsInterface(interfaceId);
//     }

//     // IERC2981
//     function royaltyInfo(uint256 _tokenId, uint256 _salePrice) external view override returns (address, uint256 royaltyAmount) {
//         _tokenId; // silence solc warning
//         royaltyAmount = _salePrice * 10 / 100;  // 10%
//         return (coreTeam_1, royaltyAmount);
//     }


//     // Contract Control _ ADMIN ONLY
//     function setBaseURI(string memory _newBaseURI) external onlyOwner{
//         baseURI = _newBaseURI;
//     }

//     function setBaseExtension(string memory _newBaseExtension) external onlyOwner {
//         baseExtension = _newBaseExtension;
//     }

//     function togglePublicSaleStatus() external onlyOwner{
//         publicSaleLive = !publicSaleLive;
//     }

//     function togglePauseStatus() external ADMIN_OR_DEFENDER{
//         if(address(coreTeam_1) == address(0)) { revert Pause_MustSetAllVariablesFirst();}
//         if(address(coreTeam_2) == address(0)) { revert Pause_MustSetAllVariablesFirst();}
//         if(address(usdcTokenContract) == address(0)) { revert Pause_MustSetAllVariablesFirst();}
//         if(address(wbtcTokenContract) == address(0)) { revert Pause_MustSetAllVariablesFirst();}
//         string memory currentBaseURI = _baseURI();
//         if(bytes(currentBaseURI).length == 0) { revert Pause_BaseURIMustBeSetFirst();}

//         paused = !paused;
//     }

//     function setCoreTeamAddresses(
//         address _coreTeam_1,
//         address _coreTeam_2,
//         uint _percent_1,
//         uint _percent_2
//         ) external onlyOwner {

//         if (address(_coreTeam_1 ) == address(0) || address(_coreTeam_2 ) == address(0)) { revert Address_CantBeAddressZero();}
//         require(_percent_1 + _percent_2 <= 10, "coreTeam_1 and coreTeam_2 must be 10% or lower");
//         coreTeam_1 = _coreTeam_1;
//         coreTeam_2 = _coreTeam_2;
//         coreTeam_1_percent  = _percent_1;
//         coreTeam_2_percent  = _percent_2;
//     }

//     function setMintingPrice(uint _price) external onlyOwner {
//         if (!paused) { revert Pause_MustBePaused();}
//         mintingCost = _price;
//     }

//     function setUsdcTokenAddress(address _address) public onlyOwner {
//         if (address(_address ) == address(0)) { revert Address_CantBeAddressZero();}
//         usdcTokenContract = _address;
//     }

//     function setUsdcTokenDecimals(uint _decimals) public  onlyOwner {
//         usdcTokenDecimals = _decimals;
//     }

//     function setWbtcTokenAddress(address _address) public onlyOwner {
//         if (address(_address ) == address(0)) { revert Address_CantBeAddressZero();}
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

//     function blacklistMalicious(address account, bool value) external onlyOwner {
//         isBlacklisted[account] = value;
//     }

//     function setMonthlyMaintenanceFeePerNFT(uint256 _monthly_maint_fee_per_nft) external onlyOwner {
//         calculatedMonthlyMaintenanceFee = _monthly_maint_fee_per_nft;
//     }

//     function setStockYardInfo(uint _stockyardNumber, uint256 _startingDisperableAmount, uint _startingIndex, uint _endingIndex) public onlyOwner {
//         if (_startingIndex == 0 || _endingIndex == 0 || _stockyardNumber == 0) { revert Stockyard_BadInputParameter();}
//         if (_endingIndex > _tokenSupply.current()) { revert Stockyard_BadInputParameter();}
//         if (stockyardInfo[_stockyardNumber - 1].endingIndex + 1 != _startingIndex ) { revert Stockyard_BadInputParameter();}
   
//         stockyardInfo[_stockyardNumber] =  StockyardInfo(_startingIndex, _endingIndex,_startingDisperableAmount);
//     }



// }


