// // SPDX-License-Identifier: MIT
// pragma solidity 0.8.7;

// /*    
// 🅣🅗🅔🅡🅐🅝🅒🅗_🅑🅤🅛🅛🅢_➋⓿➋➋
// */

// import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
// import "@chainlink/contracts/src/v0.8/interfaces/VRFCoordinatorV2Interface.sol";
// import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol";
// import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
// import "@openzeppelin/contracts/access/Ownable.sol";
// import "@openzeppelin/contracts/utils/Counters.sol";
// import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
// import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
// import { IERC2981, IERC165 } from "@openzeppelin/contracts/interfaces/IERC2981.sol";


// error Minting_ExceedsTotalBulls();
// error Minting_ExceedsMintingLimitPerAddress();
// error Minting_PublicSaleNotLive();
// error Minting_IsZeroOrBiggerThanTen();
// error Contract_CurrentlyPaused_CheckSocials();
// error Pause_MustSetAllVariablesFirst();
// error Pause_BaseURIMustBeSetFirst();
// error Pause_MustBePaused();
// error Rewarding_NotReady();
// error Rewarding_SkippingOrDoubleRewarding();
// error Rewarding_HasAlreadyHappenedThisMonth();
// error Maintenance_UpdatingNotReady();
// error Maintenance_NoMaintenanceFeesRequired();
// error Liquidation_NothingToDo();
// error BadLogicInputParameter();
// error Stockyard_IsNotSetYet();
// error Partner_NotAllowed();
// error Address_CantBeAddressZero();
// error Blacklisted();
// error Rewarding_NoBalanceToWithdraw();

// contract TheRanchBullsMintReward is 
//     VRFConsumerBaseV2,
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

//     //gnosis-safe address 
//     address public hostingSafe;
//     address public btcMinersSafe;

//     // Minting 
//     uint public constant maxSupply = 10000;
//     uint256 public mintingCost = 350;  // USDC.e
//     uint256 public nftPerAddressLimit = 50;
//     mapping(address => uint256) public addressMintCount; // how many times has this address minted an NFT from this contract. 

//     bool public publicSaleLive = false;
//     bool public paused = true;

//     mapping(address => bool) public isBlacklisted;

//     mapping(address => uint) public userMintCount;  // How many bulls did an address mint
//     mapping(address => bool) public userInDailyRaffle;  // Is the person already in the daily raffle?

//     mapping(address => address) public myPartner;   // partner mapping; msg.sender  ==> who referred them
//     mapping(address => uint256) public myParnterNetworkTeam;   // partner mapping; msg.sender  ==> who referred them

//     // Contract Balances
//     uint256 public btcMinersSafeBalance;
//     uint256 public hostingSafeBalance;     // reserve kept for hosting fees and will be used if people don't pay their maintenance fees on time
//     uint256 public USDCRewardsBalance;    // amount held within contract for referrals and raffle balance 
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


//     /**
//      * @dev For addresses that are more than 3 months behind on the maintenance fees, each 
//      * each address added here will get liquidated
//     */
//     address[] internal upForLiquidation; 

//     // Stockyard allows the rewardBulls function to be more modular. 
//     struct StockyardInfo {
//         uint startingIndex;
//         uint endingIndex;
//     }

//     mapping (uint => StockyardInfo) public stockyardInfo;

 

//     // BTC Bull Owners information 
//     struct BTCBullOwner {
//         uint256 USDC_Balance;
//         uint256 WBTC_Balance;
//         uint256 maintenanceFeeBalance;    
//         uint maintenanceFeesStanding;     // how many months are they behind on the maintenance fees? 0 means all paid up, 4 gets liquidated.
//         uint lastRewardDate;        // this tracks when the last time I rewarded them. Aug 2022 would be 0822, Mar 2023 would be 0323. 
//     }

//     mapping(address => BTCBullOwner) public btcBullOwners;



//     // Monthly WBTC rewarding variables 

//     uint public currentRewardingDate;        // This date is set when we send WBTC into the contract to reward the BTC Bulls to confirm who has been paid out. 
//     uint public stockyardsThatHaveBeenRewardedCount;  // security check to make sure we don't rewarding the same stockyard twice or skip a stockyard
//     uint256 public payPerNftForTheMonth;      // Total Monday WBTC deposit / totalSupply()
//     uint256 public lastDeposit;         // variable that tracks last deposit. If not reset after rewarding, it keeps serves as a check to deposit money and start rewarding
//     address[] public rewardedAddresses;  // array for address if we have EVER rewarded them. 
//     bool public readyToReward;   // bool to confirm we have met all the requirements and are good to go to call the rewardBulls function 



//     /**
//      * @dev The isEcosystemRole is for other contracts that are allowed to update the USDC for BTC BULL Owners on this contract.
//      * @dev The isDefenderRole our openzeppelin Defender account working with autotasks and sentinals.
//     */
//     mapping(address => bool) public isEcosystemRole;
//     mapping(address => bool) public isDefenderRole;


//     modifier ADMIN_OR_DEFENDER {
//         require(msg.sender == owner() || isDefenderRole[msg.sender] == true, "Caller is not an OWNER OR DEFENDER");
//         _;
//     }

//     /* Events */
//     event RequestedRaffleWinner(uint256 indexed requestId);

//     event PauseChanged(address _account, bool _changedTo);

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

//     event rewardEvent(
//             uint256 payPerNftForTheMonth,
//             uint256 maintenanceFeesForEachNFT,
//             uint indexed startingIndex,
//             uint indexed endingIndex
//     );

//     event resetRewardEvent(
//         address caller,
//         string sectionMessage
//     );

//      event setPayPerNFTEvent(
//         uint256 totalDeposit,
//         uint256 calculatedPayPerNFT,
//         uint rewardDate
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
//         ERC721("TheRanch_BTC_BULLS_COMMUNITY", "TRBC") {



//         if (address(_coreTeam_1) == address(0)) { revert Address_CantBeAddressZero();}
//         if (address(_coreTeam_2) == address(0)) { revert Address_CantBeAddressZero();}
//         coreTeam_1 = _coreTeam_1;
//         coreTeam_2 = _coreTeam_2;
        
//         setBaseURI(_initBaseURI);  
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
//      * 0. Only works if not paused
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
//         if (_tokenSupply.current() + _tokenQuantity > maxSupply) {revert Minting_ExceedsTotalBulls();}
//         if (addressMintCount[msg.sender] + _tokenQuantity > nftPerAddressLimit) { revert Minting_ExceedsMintingLimitPerAddress();}


//         IERC20 usdcToken = IERC20(usdcTokenContract);
//         uint256 minting_cost_per_bull = mintingCost * 10 ** usdcTokenDecimals;
//         uint256 totalTransactionCost = minting_cost_per_bull * _tokenQuantity;
//         usdcToken.safeTransferFrom(msg.sender, address(this), (totalTransactionCost));

//         for(uint256 i = 0; i < _tokenQuantity; i++) {
//             _tokenSupply.increment();
//             addressMintCount[msg.sender] += 1;
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
//         uint256 hostingSafeAmt = totalTransactionCost * 5 / 100;
//         uint256 btcMinersSafeAmt = totalTransactionCost - (referralFundAmt + raffleFundAmt)  - hostingSafeAmt; 
//         USDCRewardsBalance += (referralFundAmt + raffleFundAmt);
//         btcMinersSafeBalance += btcMinersSafeAmt;
//         hostingSafeBalance += hostingSafeAmt; 
        
//         // update USDC Reward Balances for referrals
//         address referrer = myPartner[msg.sender];
//         if(referrer != address(0) && userMintCount[referrer] > 0){
//             //updateUsdcBonus(referrer, referralFundAmt);
//             btcBullOwners[referrer].USDC_Balance += referralFundAmt;
//         }
//         else
//         {
//             uint256 splitReferralAmt = referralFundAmt * 50 / 100;
//             // updateUsdcBonus(coreTeam_1, splitReferralAmt);
//             // updateUsdcBonus(coreTeam_2, splitReferralAmt);
//             btcBullOwners[coreTeam_1].USDC_Balance += splitReferralAmt;
//             btcBullOwners[coreTeam_2].USDC_Balance += splitReferralAmt;
//         }
        
//         emit NewBullsEnteringRanch(msg.sender,_enterRaffle, _tokenQuantity, _tokenSupply.current());
//     }



//     function setReadyToReward() external ADMIN_OR_DEFENDER {
//         if (calculatedMonthlyMaintenanceFee == 0) { revert Rewarding_NotReady();}
//         if (payPerNftForTheMonth == 0) { revert Rewarding_NotReady();}

//         readyToReward = true;
//     }

//     function resetReadyToRewardChecks() external ADMIN_OR_DEFENDER {
//         readyToReward = false;
//         payPerNftForTheMonth = 0;
//         calculatedMonthlyMaintenanceFee = 0;
//         stockyardsThatHaveBeenRewardedCount = 0;
//         lastDeposit = 0;
//         emit resetRewardEvent(msg.sender, "Reset Rewarding Variables");
//     }




//     // This need to be done in a single transaction. The problem is that if we try this in multiple transactions, this
//     // would end up re-updating the payPerNftForTheMonth and the total payout to each NFT owner would be messed up. 
//     // The only way to deposit more money into this function and update the payPerNftForTheMonth variable would be to run
//     // through the rewarding, which then sets the lastDeposit back to zero and doing another round of rewarding for the month.

//     function setPayPerNftForTheMonthAndCurrentRewardingDate(uint256 _totalAmountToDeposit, uint _dateOfRewarding) public onlyOwner {
//         if (lastDeposit != 0) { revert Rewarding_HasAlreadyHappenedThisMonth();}
//         if (_dateOfRewarding == currentRewardingDate) { revert Rewarding_HasAlreadyHappenedThisMonth();}


//         IERC20 tokenContract = IERC20(wbtcTokenContract);
//         tokenContract.safeTransferFrom(msg.sender, address(this), _totalAmountToDeposit);
        
//         currentRewardingDate = _dateOfRewarding;
//         lastDeposit = _totalAmountToDeposit;

        
//         // in this function, lets pay out the core team first and then the 90% left gets divided up. 
//         uint256 coreTeam_1_amt = _totalAmountToDeposit * coreTeam_1_percent / 100;
//         uint256 coreTeam_2_amt = _totalAmountToDeposit * coreTeam_2_percent / 100;

//         uint256 _disperableAmount = (_totalAmountToDeposit * (100 - (coreTeam_1_percent + coreTeam_2_percent)) / 100); 
//         uint256 payout_per_nft = _disperableAmount / _tokenSupply.current();
//         payPerNftForTheMonth = payout_per_nft;

//         btcBullOwners[coreTeam_1].WBTC_Balance += coreTeam_1_amt;
//         btcBullOwners[coreTeam_2].WBTC_Balance += coreTeam_2_amt;

//         // emit event 
//         emit setPayPerNFTEvent(_totalAmountToDeposit, payout_per_nft, _dateOfRewarding);
        

//     }   


//     /** 
//     * @dev  check all address who have been rewarded. If there lastRewardYearMonth isn't the currentRewardingDate, then lets investigate. If they have a WBTC balance, then we need
//     * to update there maintenanceFeesStanding by 1 and add to liquidation list if they reach 4 in that category 
//     */
//     function updateMaintenanceStanding() external ADMIN_OR_DEFENDER {
//         for( uint i; i < rewardedAddresses.length; i++) {
//             address _wallet = rewardedAddresses[i];
//             if (btcBullOwners[_wallet].WBTC_Balance > 0){
//                 if (btcBullOwners[_wallet].lastRewardDate != currentRewardingDate) {

//                     // take action and add one to maintenanceFeesStanding
//                     btcBullOwners[_wallet].maintenanceFeesStanding += 1;

//                     if (btcBullOwners[_wallet].maintenanceFeesStanding == 4){
//                         upForLiquidation.push(_wallet);
//                     }
//                 }
//             }
//         }
//     }


//      /**
//     * @dev The Reward function is a modular setup so we can go through all the NFTs in multiple passes to circumvent gas problems. 
//     * 1. Only works if the readyToReward varible is true, that means all the admin tasks before rewarding have taken place.  
//     * 2. updates the stockyardsThatHaveBeenRewardedCount variable to make sure we can't call the reward on the same stockyard multiple times. 
//     * 3. checks the currentRewardDate for the owner's account, only lets them pass throught he function is its differnt than the current date. this allows for a single pass for that wallet and skips if they own more than one.
//     * 4. Checks to see if we have every rewarded them by detecting is there lastRewardDate is not initialized yet. 
//     * 5. updates the lastRewardDate for the account
//     * 6. rewards user for all the NFTs the currently own on the contract. 
//     * 7. updates WBTC balance for the user and a percentage is sent to their parnters account if thats set, to the core team if partner is not set. 
//     * 8. updates the maintenance Fee balance that the user owes for the months (hosting fees at the mining facility)
//     * 9. updates the maintenanceFeesStanding for the user, if this number is 4 then they are up for liquidation and pushed to that array to be in queue for liquidating them
//     * 10. emits event showing how much we paid for each NFT, how much the maintenance fee for each NFT was, the starting index and ending index we rewarded during the function. 
//     */

//     function rewardBulls(uint _stockyardNumber) public payable ADMIN_OR_DEFENDER {
   
//         if (readyToReward == false) { revert Rewarding_NotReady();}
//         if (!paused) { revert Pause_MustBePaused();}
//         if (_stockyardNumber != stockyardsThatHaveBeenRewardedCount + 1) { revert Rewarding_SkippingOrDoubleRewarding();}

//         stockyardsThatHaveBeenRewardedCount++ ;

//         uint startingIndex = stockyardInfo[_stockyardNumber].startingIndex;
//         uint endingIndex = stockyardInfo[_stockyardNumber].endingIndex;

//         for( uint i = startingIndex; i <= endingIndex; i++) {
//             address bullOwnerAddress = ownerOf(i);
            
//             if (bullOwnerAddress != address(0)){

//                 // have we checked them this month, if lastRewardDate == currentRewardingDate then skip them  
//                 if (btcBullOwners[bullOwnerAddress].lastRewardDate != currentRewardingDate) {


//                     // Have we ever rewarded them before, if not, add them into the rewarded address array. 
//                     if (btcBullOwners[bullOwnerAddress].lastRewardDate == 0) {
//                         rewardedAddresses.push(bullOwnerAddress);
//                     }

//                     BTCBullOwner storage _bullOwner = btcBullOwners[bullOwnerAddress];

//                     // update lastRewardDate for this address 
//                     _bullOwner.lastRewardDate = currentRewardingDate;
        

//                     // get the amount of NFTs this address owns
//                     uint _nftCount = walletOfOwner(bullOwnerAddress).length;

//                     // get the total payout amound
//                     uint256 totalPayoutForTheBullOwner = _nftCount * payPerNftForTheMonth;
                    
//                     // get the referr and the referral amount 
//                     address referrer = myPartner[bullOwnerAddress];
//                     uint256 referralAmt = totalPayoutForTheBullOwner * 1 / 100;

//                     // update the wbtc balances accordingly with their partner 
//                     if(referrer != address(0) && userMintCount[referrer] > 0){
//                         btcBullOwners[referrer].WBTC_Balance += referralAmt;
//                         _bullOwner.WBTC_Balance += (totalPayoutForTheBullOwner - referralAmt);
      
    
//                     } else {
//                         btcBullOwners[coreTeam_1].WBTC_Balance += referralAmt;
//                         btcBullOwners[coreTeam_2].WBTC_Balance += referralAmt;
//                         _bullOwner.WBTC_Balance += (totalPayoutForTheBullOwner - (referralAmt * 2));
         
//                     }

//                     //  update the maintenance Fees due from the _bullOwner
//                     _bullOwner.maintenanceFeeBalance += (_nftCount * calculatedMonthlyMaintenanceFee);
         

//                     // update the maintenanceFeesStanding for the _bullOwner
//                     _bullOwner.maintenanceFeesStanding += 1;


//                     // Check if _bullOwner is more than 3 months behind on the account 
//                     if (_bullOwner.maintenanceFeesStanding == 4){
//                         upForLiquidation.push(bullOwnerAddress);
//                     }
//                 }
//             }
//         }

//         emit rewardEvent(payPerNftForTheMonth, calculatedMonthlyMaintenanceFee, startingIndex, endingIndex);
//     }



//     /**
//     * @dev When any other contract in our ecosystem checks the owner of the BTC Bulls, it will updated the USDC amount for the 
//     * BTC Bulls owner on this contract. It incentives ownership of both NFTS this way: 
//     * In this example, lets assume we have a HayBale NFT on another smart contract, 
//     * - if the HayBale owner also owns a Bull NFT on this contract, they'll get amtToDistribute  == _amountToAdd, then we look for the partner of that address and do a 95/5 approach,
//     *   95% go to the owner and 5% goes to the partner.
//     * -if the Haybale owner does not own a bull, they'll get 70% of the _amountToAdd while 5% goes to core1 and core2 and 20% to the hostingSafe Balance
  
//     */
//     function updateUsdcBonusFromAnotherContract(address[] memory _ownersOfTheNFTs, uint256 _amountToAdd) external {
//         require(isEcosystemRole[msg.sender] == true, "must be approved to interact");

//         for( uint i; i < _ownersOfTheNFTs.length; i++) {
//             address _ownerOfNFT = _ownersOfTheNFTs[i];

//             // this address does own a BTC Bull
//             if (balanceOf(_ownerOfNFT) > 0){
//                 //btcBullOwners[_ownerOfNFT].USDC_Balance += _amountToAdd;

//                 // get the referr of this particular BTC Bull owner  
//                 address referrer = myPartner[_ownerOfNFT];
//                 uint256 referralAmt = _amountToAdd * 5 / 100;

//                 // update the usdc  balances accordingly with their partner 
//                 if(referrer != address(0) && userMintCount[referrer] > 0){
//                     btcBullOwners[referrer].USDC_Balance += referralAmt;
//                     btcBullOwners[_ownerOfNFT].USDC_Balance += (_amountToAdd - referralAmt);
    
//                 } else {
//                     btcBullOwners[coreTeam_1].USDC_Balance += referralAmt;
//                     btcBullOwners[coreTeam_2].USDC_Balance += referralAmt;
//                     btcBullOwners[_ownerOfNFT].USDC_Balance += (_amountToAdd - (referralAmt * 2));
//                 }

//             // this address does NOT own a BTC Bull
//              } else {
//                 uint256 deductionAmt = _amountToAdd * 5 / 100;

//                 btcBullOwners[coreTeam_1].USDC_Balance += deductionAmt;
//                 btcBullOwners[coreTeam_2].USDC_Balance += deductionAmt;
//                 hostingSafeBalance += (deductionAmt * 4);
//                 btcBullOwners[_ownerOfNFT].USDC_Balance += (_amountToAdd - (deductionAmt * 6));
//             }
//         }
//     }



//     function getLiquidatedArrayLength() public view ADMIN_OR_DEFENDER returns (uint) {
//         return upForLiquidation.length;
//     }

//     /**
//      * @dev If the user has been added to the liquidityArray, that means they are 4 months behind on paying their maintenance fees
//      * Liquidating them means transfering the WBTC out of their account and sending it the Hosting Safe Multisig wallet. 
//     **/
//     function liquidateOutstandingAccounts() external ADMIN_OR_DEFENDER {
//         if (!paused) { revert Maintenance_UpdatingNotReady();}
//         if (upForLiquidation.length < 1) { revert Liquidation_NothingToDo();}

//         uint256 totalAmountLiquidated; 

//         for( uint i; i < upForLiquidation.length; i++) {
//             address _culprit = upForLiquidation[i];
//             uint256 _amount = btcBullOwners[_culprit].WBTC_Balance;
//             btcBullOwners[_culprit].WBTC_Balance = 0;
//             totalAmountLiquidated += _amount; 

//             // reset fees and months behind. 
//             btcBullOwners[_culprit].maintenanceFeeBalance = 0;
//             btcBullOwners[_culprit].maintenanceFeesStanding = 0;
            
//             // emit event
//             emit liquidationEvent(_culprit, _amount) ;
            
//         }

//         upForLiquidation = new address[](0);

//         IERC20 tokenContract = IERC20(wbtcTokenContract);
//         tokenContract.approve(address(this), totalAmountLiquidated);
//         tokenContract.safeTransferFrom(address(this), hostingSafe, totalAmountLiquidated);
//     }


//     /**
//      * @dev If the user has USDC rewards to within their account
//      * the maintanence fee balance will be deducted from that. 
//      * If it doesn't cover the entire maintenance fee cost, 
//      * the rest of the amount will be asked to beapproved and sent to the contract. 
//     **/
//     function payMaintanenceFees() external nonReentrant {

//         uint256 _feesDue = btcBullOwners[msg.sender].maintenanceFeeBalance;
//         uint256 _balance = btcBullOwners[msg.sender].USDC_Balance;
        
//         if (_feesDue == 0) { revert Maintenance_NoMaintenanceFeesRequired();}

//         if (_balance >= _feesDue){

//             btcBullOwners[msg.sender].USDC_Balance -= _feesDue;
//             hostingSafeBalance += _feesDue; 

//             emit payMaintanenceFeesEvent(msg.sender, _feesDue, 0);
//         } else {

//             uint256 amt_needed =  _feesDue - _balance;
//             if(_balance == 0){
//                 IERC20 usdcToken = IERC20(usdcTokenContract);
//                 usdcToken.safeTransferFrom(msg.sender, address(this), (_feesDue));
//                 hostingSafeBalance += _feesDue; 
//             } else {
                
//                 btcBullOwners[msg.sender].USDC_Balance -= _balance; 

//                 IERC20 usdcToken = IERC20(usdcTokenContract);
//                 usdcToken.safeTransferFrom(msg.sender, address(this), (amt_needed));

//                 hostingSafeBalance += (amt_needed + _balance); 
//             }

//             emit payMaintanenceFeesEvent(msg.sender, _balance, amt_needed);
//         }

//         // reset fees and months behind. 
//         btcBullOwners[msg.sender].maintenanceFeeBalance = 0;
//         btcBullOwners[msg.sender].maintenanceFeesStanding = 0;

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
//         address dailyRaffleWinner = dailyRafflePlayers[indexOfWinner];
        
//         // update the daily raffle winnners USDC balance
//         btcBullOwners[dailyRaffleWinner].USDC_Balance += dailyRaffleBalance;

//         resetUserInDailyRaffle(); // must do before resetting dailyRafflePlayers
//         dailyRaffleBalance = 0;  // reset dailyRaffleBalance back to zero after drawing
//         dailyRafflePlayers = new address[](0);

//         emit dailyRaffleWinnerEvent(dailyRaffleWinner, dailyRaffleBalance);

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

//     function withdraw() external onlyOwner {
//         payable(msg.sender).transfer(address(this).balance);
//     }

//     function withdrawToken(address _tokenContract, uint256 _amount) external onlyOwner {
//         IERC20 tokenContract = IERC20(_tokenContract);
//         tokenContract.safeTransfer(msg.sender, _amount);
//     }

//     function withdrawBtcMinersSafeBalance() external ADMIN_OR_DEFENDER {
//         IERC20 tokenContract = IERC20(usdcTokenContract);
//         uint256 amtToTransfer = btcMinersSafeBalance;
//         tokenContract.approve(address(this), amtToTransfer);
//         tokenContract.safeTransferFrom(address(this), btcMinersSafe, amtToTransfer);
//         btcMinersSafeBalance -= amtToTransfer;

    
//     }

//     function withdrawHostingSafeBalance() external ADMIN_OR_DEFENDER {
//         IERC20 tokenContract = IERC20(usdcTokenContract);
//         uint256 amtToTransfer = hostingSafeBalance;
//         tokenContract.approve(address(this), amtToTransfer);
//         tokenContract.safeTransferFrom(address(this), hostingSafe, amtToTransfer);
//         hostingSafeBalance -= amtToTransfer;
//     }


//     function withdrawWbtcForWalletAddress() external nonReentrant {
//         if (paused) { revert Contract_CurrentlyPaused_CheckSocials();}
//         if (isBlacklisted[msg.sender]) { revert Blacklisted();}

//         require(btcBullOwners[msg.sender].maintenanceFeeBalance == 0, "You must pay maintenance fee balance before WBTC withdrawal is allowed");

//         // Get the total Balance to award the owner of the NFT(s)
//         uint256 myBalance = btcBullOwners[msg.sender].WBTC_Balance; 
//         if (myBalance == 0) { revert Rewarding_NoBalanceToWithdraw();}

//         // Transfer Balance 
//         IERC20(wbtcTokenContract).safeTransfer(msg.sender, myBalance );

//         // update wbtc balance for nft owner
//         btcBullOwners[msg.sender].WBTC_Balance = 0;
        
//         emit withdrawWbtcRewardsEvent(msg.sender, myBalance);
//     }

//     function withdrawUsdcRewardBalance() external nonReentrant {
//         if (paused) { revert Contract_CurrentlyPaused_CheckSocials();}
//         if (isBlacklisted[msg.sender]) { revert Blacklisted();}
        
//         // Get USDC rewards balance for msg.sender
//         uint256 myBalance = btcBullOwners[msg.sender].USDC_Balance;
//         if (myBalance == 0) { revert Rewarding_NoBalanceToWithdraw();}
 
//         // Transfer Balance 
//         IERC20(usdcTokenContract).safeTransfer(msg.sender, (myBalance));
//         // update mapping on contract 

//         btcBullOwners[msg.sender].USDC_Balance = 0  ;
        
//         // update USDC Rewards Balance Total
//         USDCRewardsBalance -= myBalance;
        
//         // emit event
//         emit withdrawUSDCRewardsForAddressEvent(msg.sender, myBalance);
        
//     }



//     /** Getter Functions */


//     /**
//      * @dev returns how many people have ever been rewarded from owning a BTC Bull
//      */
//     function getRewardAddressesLength() public view returns (uint){
//         return rewardedAddresses.length;
//     }

//     function getMaintenanceFeesForTheOwner() public view returns (uint256){
//         return btcBullOwners[msg.sender].maintenanceFeeBalance;
//     }

//     function getMaintenanceFeesStandingForTheOwner() public view returns (uint){
//         return btcBullOwners[msg.sender].maintenanceFeesStanding;
//     }


//     function getWbtcBalanceForTheOwner() public view returns (uint256){
//         return btcBullOwners[msg.sender].WBTC_Balance;
//     }


//     function getUsdcRewardBalanceForTheOwner() public view returns (uint256) {
//         return btcBullOwners[msg.sender].USDC_Balance;
//     }

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

//     function getRafflePlayer(uint256 index) public view returns (address) {
//         return dailyRafflePlayers[index];
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
//     function supportsInterface(bytes4 interfaceId) public view override(ERC721Enumerable, IERC165) returns (bool) {
//         return interfaceId == type(IERC2981).interfaceId || super.supportsInterface(interfaceId);
//     }

//     // IERC2981
//     function royaltyInfo(uint256 _tokenId, uint256 _salePrice) external view override returns (address, uint256 royaltyAmount) {
//         _tokenId; // silence solc warning
//         royaltyAmount = _salePrice * 10 / 100;  // 10%
//         return (coreTeam_1, royaltyAmount);
//     }


//     // Contract Control _ ADMIN ONLY
//     function setBaseURI(string memory _newBaseURI) public onlyOwner{
//         baseURI = _newBaseURI;
//     }

//     function setBaseExtension(string memory _newBaseExtension) external onlyOwner {
//         baseExtension = _newBaseExtension;
//     }

//     function togglePublicSaleStatus() external onlyOwner{
//         publicSaleLive = !publicSaleLive;
//     }

//     function setPauseStatus(bool _paused) external ADMIN_OR_DEFENDER{
//         if(address(coreTeam_1) == address(0)) { revert Pause_MustSetAllVariablesFirst();}
//         if(address(coreTeam_2) == address(0)) { revert Pause_MustSetAllVariablesFirst();}
//         if(address(usdcTokenContract) == address(0)) { revert Pause_MustSetAllVariablesFirst();}
//         if(address(wbtcTokenContract) == address(0)) { revert Pause_MustSetAllVariablesFirst();}
//         if(address(hostingSafe) == address(0)) { revert Pause_MustSetAllVariablesFirst();}
//         if(address(btcMinersSafe) == address(0)) { revert Pause_MustSetAllVariablesFirst();}
//         string memory currentBaseURI = _baseURI();
//         if(bytes(currentBaseURI).length == 0) { revert Pause_BaseURIMustBeSetFirst();}

//         paused = _paused;

//         emit PauseChanged(msg.sender, _paused);
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


//     function setSafeAddresses(address _hostingSafe, address _btcMinersSafe) external onlyOwner {
//         if (address(_hostingSafe ) == address(0) || address(_btcMinersSafe ) == address(0)) { revert Address_CantBeAddressZero();}
//         hostingSafe = _hostingSafe;
//         btcMinersSafe = _btcMinersSafe;
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

//     function blacklistMalicious(address _address, bool value) external onlyOwner {
//         isBlacklisted[_address] = value;
//     }

//     function setEcosystemRole(address _address, bool value) external onlyOwner {
//         isEcosystemRole[_address] = value;
//     }

//     function setDefenderRole(address _address, bool value) external onlyOwner {
//         isDefenderRole[_address] = value;
//     }

//     function setMonthlyMaintenanceFeePerNFT(uint256 _monthly_maint_fee_per_nft) external onlyOwner {
//         calculatedMonthlyMaintenanceFee = _monthly_maint_fee_per_nft;
//     }

//     function setStockYardInfo(uint _stockyardNumber, uint _startingIndex, uint _endingIndex) public onlyOwner {
//         if (_startingIndex == 0 || _endingIndex == 0 || _stockyardNumber == 0) { revert BadLogicInputParameter();}
//         if (_endingIndex > _tokenSupply.current()) { revert BadLogicInputParameter();}
//         if (stockyardInfo[_stockyardNumber - 1].endingIndex + 1 != _startingIndex ) { revert BadLogicInputParameter();}
   
//         stockyardInfo[_stockyardNumber] =  StockyardInfo(_startingIndex, _endingIndex);
//     }

//     /**
//     * @dev This is the amount of rewards thats (percentage) that an owner will keep if they don't own a BTC bull on this contract
//     * when theupdateUsdcBonusFromAnotherContract function rewards the current owners of BTC Bulls via another NFT in the ecosystem. 
//     */
   
// }


