from curses import use_env
from distutils import core
from unittest import mock
from pyrsistent import v
from scripts.helpful_scripts import get_account, get_contract, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import TheRanchBullsMintAndReward, MockedTokens_USDC, MockedTokens_WBTC, network, config, MockV3Aggregator, accounts, exceptions, chain
from scripts.deploy_mintAndReward import deploy_contract
from scripts.deploy_v2mocks import deploy_v2mocks
from web3 import Web3
import time, pytest
import pprint
import math






def test_():

    fund_deposited = 80_000

    #owner = accounts[0]
    owner = get_account()
    TheRanchBullsMintAndReward = deploy_contract()

    ### set the address on each contract for to reference other contract ####

 
    # assert contract_balance == 0
    
    person_1 = accounts[1]
    person_2 = accounts[2]
    person_3 = accounts[3]
    person_4 = accounts[4]
    person_5 = accounts[5]
    person_6 = accounts[6]
    person_7 = accounts[7]
    person_8 = accounts[8]
    person_9 = accounts[9]
    person_10 = accounts[10]
    person_11 = accounts[11]
    person_12 = accounts[12]
    person_13 = accounts[13]
    person_14 = accounts[14]
    person_15 = accounts[15]
    person_16 = accounts[16]
    person_17 = accounts[17]
    person_18 = accounts[18]
    person_19 = accounts[19]
    person_20 = accounts[20]
    person_21 = accounts[21]
    person_22 = accounts[22]
    person_23 = accounts[23]
    person_24 = accounts[24]
    person_25 = accounts[25]
    person_26 = accounts[26]
    person_27 = accounts[27]
    person_28 = accounts[28]
    person_29 = accounts[29]
    person_30 = accounts[30]

    person_31 = accounts[31]
    person_32 = accounts[32]
    person_33 = accounts[33]
    person_34 = accounts[34]
    person_35 = accounts[35]
    person_36 = accounts[36]
    person_37 = accounts[37]
    person_38 = accounts[38]
    person_39 = accounts[39]
    person_40 = accounts[40]

    person_41 = accounts[41]
    person_42 = accounts[42]
    person_43 = accounts[43]
    person_44 = accounts[44]
    person_45 = accounts[45]
    person_46 = accounts[46]
    person_47 = accounts[47]
    person_48 = accounts[48]
    person_49 = accounts[49]
    person_50 = accounts[50]

    person_51 = accounts[51]
    person_52 = accounts[52]
    person_53 = accounts[53]
    person_54 = accounts[54]
    person_55 = accounts[55]
    person_56 = accounts[56]
    person_57 = accounts[57]
    person_58 = accounts[58]
    person_59 = accounts[59]
    person_60 = accounts[60]
 
    person_61 = accounts[61]
    person_62 = accounts[62]
    person_63 = accounts[63]
    person_64 = accounts[64]
    person_65 = accounts[65]
    person_66 = accounts[66]
    person_67 = accounts[67]
    person_68 = accounts[68]
    person_69 = accounts[69]
    person_70 = accounts[70]

    person_71 = accounts[71]
    person_72 = accounts[72]
    person_73 = accounts[73]
    person_74 = accounts[74]
    person_75 = accounts[75]
    person_76 = accounts[76]
    person_77 = accounts[77]
    person_78 = accounts[78]
    person_79 = accounts[79]
    person_80 = accounts[80]

    person_81 = accounts[81]
    person_82 = accounts[82]
    person_83 = accounts[83]
    person_84 = accounts[84]
    person_85 = accounts[85]
    person_86 = accounts[86]
    person_87 = accounts[87]
    person_88 = accounts[88]
    person_89 = accounts[89]
    person_90 = accounts[90]

    person_91 = accounts[91]
    person_92 = accounts[92]
    person_93 = accounts[93]
    person_94 = accounts[94]
    person_95 = accounts[95]
    person_96 = accounts[96]
    person_97 = accounts[97]
    person_98 = accounts[98]
    person_99 = accounts[99]
    person_100 = accounts[100]







    coinbase = accounts[101]
    coreTeam1 = accounts[102]
    coreTeam2 = accounts[103]


    people = {
        person_1: 'person_1',
        person_2: 'person_2',
        person_3: 'person_3',
        person_4: 'person_4',
        person_5: 'person_5',
        person_6: 'person_6',
        person_7: 'person_7',
        person_8: 'person_8',
        person_9: 'person_9',
        person_10: 'person_10',
        person_11: 'person_11',
        person_12: 'person_12',
        person_13: 'person_13',
        person_14: 'person_14',
        person_15: 'person_15',
        person_16: 'person_16',
        person_17: 'person_17',
        person_18: 'person_18',
        person_19: 'person_19',
        person_20: 'person_20',
        person_21: 'person_21',
        person_22: 'person_22',
        person_23: 'person_23',
        person_24: 'person_24',
        person_25: 'person_25',
        person_26: 'person_26',
        person_27: 'person_27',
        person_28: 'person_28',
        person_29: 'person_29',

        person_30: 'person_30',
        person_31: 'person_31',
        person_32: 'person_32',
        person_33: 'person_33',
        person_34: 'person_34',
        person_35: 'person_35',
        person_36: 'person_36',
        person_37: 'person_37',
        person_38: 'person_38',
        person_39: 'person_39',

        person_40: 'person_40',
        person_41: 'person_41',
        person_42: 'person_42',
        person_43: 'person_43',
        person_44: 'person_44',
        person_45: 'person_45',
        person_46: 'person_46',
        person_47: 'person_47',
        person_48: 'person_48',
        person_49: 'person_49',

        person_50: 'person_50',
        person_51: 'person_51',
        person_52: 'person_52',
        person_54: 'person_54',
        person_55: 'person_55',
        person_55: 'person_55',
        person_56: 'person_56',
        person_57: 'person_57',
        person_58: 'person_58',
        person_59: 'person_59',

        person_60: 'person_60',
        person_61: 'person_61',
        person_62: 'person_62',
        person_63: 'person_63',
        person_64: 'person_64',
        person_65: 'person_65',
        person_66: 'person_66',
        person_67: 'person_67',
        person_68: 'person_68',
        person_69: 'person_69',

        person_70: 'person_70',
        person_71: 'person_71',
        person_72: 'person_72',
        person_73: 'person_73',
        person_74: 'person_74',
        person_75: 'person_75',
        person_76: 'person_76',
        person_77: 'person_77',
        person_78: 'person_78',
        person_79: 'person_79',

        person_80: 'person_80',
        person_81: 'person_81',
        person_82: 'person_82',
        person_83: 'person_83',
        person_84: 'person_84',
        person_85: 'person_85',
        person_86: 'person_86',
        person_87: 'person_87',
        person_88: 'person_88',
        person_89: 'person_89',

        person_90: 'person_90',
        person_91: 'person_91',
        person_92: 'person_92',
        person_93: 'person_93',
        person_94: 'person_94',
        person_95: 'person_95',
        person_96: 'person_96',
        person_97: 'person_97',
        person_98: 'person_98',
        person_99: 'person_99',
        person_100: 'person_100',

     
        
    }



  
    starting_balance_of_each_account = 50_000 * 10**18


    mocked_usdc = MockedTokens_USDC.deploy(1_000_000_000 * 10**6, {"from": coinbase})


    #######################################################
    #### set the token to use for minting and rewarding ###
    #######################################################

   
    TheRanchBullsMintAndReward.setUsdcTokenAddress(mocked_usdc,{"from": owner})
    TheRanchBullsMintAndReward.setWbtcTokenAddress(mocked_usdc,{"from": owner})
    
    # print(f'usdc address : {mocked_usdc.address}')
    # print(f'dai address :  {mocked_dai.address}')
    # print(f'TotalSupplyOfTokens: {mocked_tokens_usdc.totalSupply()/10**18}')
    print(f'CoinbaseMock USDC Balance: {mocked_usdc.balanceOf(coinbase) / 10**6}')
 
    print(f'TheRanchBullsMintAndReward_ETH_balance: {TheRanchBullsMintAndReward.balanceOf(TheRanchBullsMintAndReward) /10**18}')
  
    assert (mocked_usdc.balanceOf(coinbase) / 10**6) == 1_000_000_000


    #########################################################
    ####       Transfer USDC  each person                ####
    #########################################################
    

    mocked_usdc.transfer(person_1, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_2, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_3, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_4, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_5, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_6, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_7, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_8, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_9, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_10, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_11, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_12, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_13, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_14, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_15, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_16, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_17, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_18, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_19, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_20, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_21, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_22, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_23, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_24, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_25, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_26, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_27, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_28, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_29, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_30, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_31, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_32, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_33, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_34, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_35, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_36, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_37, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_38, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_39, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_40, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_41, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_42, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_43, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_44, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_45, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_46, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_47, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_48, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_49, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_50, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_51, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_52, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_53, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_54, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_55, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_56, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_57, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_58, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_59, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_60, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_61, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_62, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_63, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_64, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_65, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_66, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_67, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_68, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_69, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_70, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_71, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_72, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_73, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_74, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_75, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_76, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_77, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_78, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_79, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_80, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_81, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_82, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_83, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_84, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_85, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_86, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_87, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_88, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_89, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_90, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_91, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_92, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_93, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_94, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_95, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_96, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_97, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_98, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_99, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_100, 100_000 * 10**6, {"from": coinbase})


    ### set coreTeam wallets ###
    TheRanchBullsMintAndReward.setCoreTeam_1_Address(coreTeam1,{"from": owner})
    TheRanchBullsMintAndReward.setCoreTeam_2_Address(coreTeam2,{"from": owner})

 
    # Owner unpauses contracts
    TheRanchBullsMintAndReward.togglePauseStatus({"from": owner})
    
    #owner starts the public sale
    TheRanchBullsMintAndReward.togglePublicSaleStatus({"from": owner})


   
    def price_needed(count):
        return (count * TheRanchBullsMintAndReward.mintingCost() * 10 ** 6)

 
    print(f'\nBEFORE: person_1 ETH Balance: {person_1.balance()/10**18}')
    print(f'BEFORE: person_1 usdc Balance: {mocked_usdc.balanceOf(person_1) / 10**6}')


    raffleEntryBool = True


    amt = 1
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_1})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_2})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_2, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_3})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_3, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_4})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_4, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_5})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_5, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_6})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_6, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_7})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_7, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_8})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_8, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_9})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_9, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_10})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_10, "value":  price_needed(amt)})
    
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_11})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_11, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_12})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_12, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_13})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_13, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_14})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_14, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_15})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_15, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_16})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_16, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_17})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_17, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_18})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_18, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_19})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_19, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_20})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_20, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_21})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_21, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_22})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_22, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_23})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_23, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_24})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_24, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_25})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_25, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_26})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_26, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_27})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_27, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_28})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_28, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_29})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_29, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_30})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_30, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_31})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_31, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_32})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_32, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_33})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_33, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_34})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_34, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_35})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_35, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_36})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_36, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_37})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_37, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_38})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_38, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_39})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_39, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_40})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_40, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_41})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_41, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_42})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_42, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_43})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_43, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_44})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_44, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_45})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_45, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_46})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_46, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_47})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_47, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_48})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_48, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_49})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_49, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_50})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_50, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_51})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_51, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_52})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_52, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_53})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_53, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_54})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_54, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_55})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_55, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_56})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_56, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_57})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_57, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_58})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_58, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_59})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_59, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_60})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_60, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_61})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_61, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_62})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_62, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_63})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_63, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_64})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_64, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_65})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_65, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_66})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_66, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_67})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_67, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_68})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_68, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_69})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_69, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_70})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_70, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_71})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_71, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_72})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_72, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_73})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_73, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_74})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_74, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_75})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_75, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_76})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_76, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_77})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_77, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_78})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_78, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_79})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_79, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_80})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_80, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_81})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_81, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_82})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_82, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_83})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_83, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_84})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_84, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_85})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_85, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_86})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_86, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_87})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_87, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_88})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_88, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_89})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_89, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_90})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_90, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_91})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_91, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_92})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_92, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_93})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_93, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_94})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_94, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_95})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_95, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_96})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_96, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_97})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_97, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_98})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_98, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_99})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_99, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_100})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_100, "value":  price_needed(amt)})
    
 
    #######################################################################
    ### Set the usdc reward Token for the contract after deploying WBTC ###
    #######################################################################

    TheRanchBullsMintAndReward.setUsdcTokenAddress(mocked_usdc, {"from": owner})
    assert TheRanchBullsMintAndReward.usdcTokenContract.call() == mocked_usdc




    assert TheRanchBullsMintAndReward.coreTeam_1_percent.call() == 8
    assert TheRanchBullsMintAndReward.coreTeam_2_percent.call() == 2

    assert TheRanchBullsMintAndReward.coreTeam_1.call() == coreTeam1
    assert TheRanchBullsMintAndReward.coreTeam_2.call() == coreTeam2




    print(f'reward token contract : {TheRanchBullsMintAndReward.wbtcTokenContract.call()}')
    
 
    ##################################################################
    ### Set the Reward Token for the contract after deploying WBTC ###
    ##################################################################

    ## deploy the wbtc contract so the owner now has wbtc in their wallet
    wbtc_decimals = 10 ** 8
    wbtc_to_start = 100
    mocked_wbtc = MockedTokens_WBTC.deploy(wbtc_to_start * wbtc_decimals, {"from": owner})
    TheRanchBullsMintAndReward.setWbtcTokenAddress(mocked_wbtc, {"from": owner})


    starting_owner_balance_wbtc = mocked_wbtc.balanceOf(owner)
    assert starting_owner_balance_wbtc == wbtc_to_start * wbtc_decimals
    assert mocked_wbtc.balanceOf(TheRanchBullsMintAndReward) == 0




    
   
    
    print("#######################################################################################")
    print(f'\t\t\t\t\t BEFORE FUNDING AND UPDATING')
    print("#######################################################################################")
    print(f'coreTeam_1 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(coreTeam1)}')
    print(f'coreTeam_2 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(coreTeam2)}')
    print(f'person_1 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_1)}')
    print(f'person_2 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_2)}')
    print(f'person_3 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_3)}')
    print(f'person_4 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_4)}')
    print(f'person_5 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_5)}')
    print(f'person_6 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_6)}')
    print(f'person_7 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_7)}')
    print(f'person_8 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_8)}')
    print(f'person_9 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_9)}')
    print(f'person_10 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_10)}')
    print(f'person_11 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_11)}')
    print(f'person_12 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_12)}')
    print(f'person_13 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_13)}')
    print(f'person_14 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_14)}')
    print(f'person_15 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_15)}')
    print(f'person_16 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_16)}')
    print(f'person_17 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_17)}')
    print(f'person_18 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_18)}')
    print(f'person_19 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_19)}')
    print(f'person_20 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_20)}')
    print(f'person_21 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_21)}')
    print(f'person_22 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_22)}')
    print(f'person_23 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_23)}')
    print(f'person_24 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_24)}')
    print(f'person_25 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_25)}')
    print(f'person_26 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_26)}')
    print(f'person_27 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_27)}')
    print(f'person_28 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_28)}')
    print(f'person_29 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_29)}')
    print(f'person_30 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_30)}')
    print(f'person_31 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_31)}')
    print(f'person_32 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_32)}')
    print(f'person_33 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_33)}')
    print(f'person_34 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_34)}')
    print(f'person_35 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_35)}')
    print(f'person_36 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_36)}')
    print(f'person_37 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_37)}')
    print(f'person_38 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_38)}')
    print(f'person_39 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_39)}')
    print(f'person_40 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_40)}')
    print(f'person_41 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_41)}')
    print(f'person_42 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_42)}')
    print(f'person_43 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_43)}')
    print(f'person_44 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_44)}')
    print(f'person_45 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_45)}')
    print(f'person_46 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_46)}')
    print(f'person_47 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_47)}')
    print(f'person_48 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_48)}')
    print(f'person_49 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_49)}')
    print(f'person_50 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_50)}')
    print(f'person_51 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_51)}')
    print(f'person_52 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_52)}')
    print(f'person_53 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_53)}')
    print(f'person_54 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_54)}')
    print(f'person_55 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_55)}')
    print(f'person_56 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_56)}')
    print(f'person_57 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_57)}')
    print(f'person_58 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_58)}')
    print(f'person_59 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_59)}')
    print(f'person_60 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_60)}')
    print(f'person_61 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_61)}')
    print(f'person_62 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_62)}')
    print(f'person_63 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_63)}')
    print(f'person_64 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_64)}')
    print(f'person_65 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_65)}')
    print(f'person_66 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_66)}')
    print(f'person_67 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_67)}')
    print(f'person_68 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_68)}')
    print(f'person_69 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_69)}')
    print(f'person_70 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_70)}')
    print(f'person_71 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_71)}')
    print(f'person_72 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_72)}')
    print(f'person_73 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_73)}')
    print(f'person_74 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_74)}')
    print(f'person_75 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_75)}')
    print(f'person_76 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_76)}')
    print(f'person_77 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_77)}')
    print(f'person_78 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_78)}')
    print(f'person_79 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_79)}')
    print(f'person_80 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_80)}')
    print(f'person_81 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_81)}')
    print(f'person_82 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_82)}')
    print(f'person_83 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_83)}')
    print(f'person_84 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_84)}')
    print(f'person_85 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_85)}')
    print(f'person_86 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_86)}')
    print(f'person_87 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_87)}')
    print(f'person_88 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_88)}')
    print(f'person_89 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_89)}')
    print(f'person_90 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_90)}')
    print(f'person_91 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_91)}')
    print(f'person_92 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_92)}')
    print(f'person_93 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_93)}')
    print(f'person_94 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_94)}')
    print(f'person_95 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_95)}')
    print(f'person_96 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_96)}')
    print(f'person_97 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_97)}')
    print(f'person_98 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_98)}')
    print(f'person_99 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_99)}')
    print(f'person_100 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_100)}')



    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_1) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_2) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_3) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_4) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_5) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_6) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_7) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_8) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_9) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_10) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_11) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_12) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_13) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_14) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_15) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_16) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_17) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_18) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_19) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_20) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_21) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_22) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_23) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_24) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_25) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_26) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_27) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_28) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_29) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_30) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_31) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_32) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_33) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_34) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_35) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_36) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_37) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_38) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_39) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_40) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_41) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_42) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_43) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_44) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_45) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_46) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_47) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_48) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_49) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_50) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_51) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_52) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_53) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_54) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_55) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_56) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_57) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_58) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_59) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_60) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_61) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_62) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_63) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_64) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_65) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_66) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_67) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_68) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_69) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_70) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_71) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_72) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_73) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_74) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_75) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_76) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_77) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_78) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_79) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_80) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_81) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_82) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_83) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_84) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_85) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_86) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_87) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_88) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_89) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_90) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_91) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_92) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_93) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_94) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_95) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_96) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_97) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_98) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_99) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_100) == 0


    print('\n')
    

    print(f'coreTeam_1 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(coreTeam1)}')
    print(f'coreTeam_2 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(coreTeam2)}')
    print(f'person_1 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_1)}')
    print(f'person_2 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_2)}')
    print(f'person_3 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_3)}')
    print(f'person_4 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_4)}')
    print(f'person_5 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_5)}')
    print(f'person_6 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_6)}')
    print(f'person_7 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_7)}')


    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_1) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_2) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_3) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_4) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_5) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_6) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_7) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_8) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_9) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_10) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_11) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_12) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_13) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_14) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_15) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_16) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_17) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_18) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_19) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_20) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_21) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_22) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_23) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_24) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_25) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_26) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_27) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_28) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_29) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_30) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_31) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_32) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_33) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_34) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_35) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_36) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_37) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_38) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_39) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_40) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_41) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_42) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_43) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_44) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_45) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_46) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_47) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_48) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_49) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_50) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_51) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_52) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_53) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_54) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_55) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_56) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_57) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_58) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_59) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_60) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_61) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_62) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_63) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_64) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_65) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_66) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_67) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_68) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_69) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_70) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_71) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_72) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_73) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_74) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_75) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_76) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_77) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_78) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_79) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_80) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_81) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_82) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_83) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_84) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_85) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_86) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_87) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_88) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_89) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_90) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_91) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_92) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_93) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_94) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_95) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_96) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_97) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_98) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_99) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_100) == 0

    print('\n')

    print(f'liquidation list: {TheRanchBullsMintAndReward.getLiquidatedArray()}')

    print('\n')

    print(f'coreTeam1 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": coreTeam1})}')
    print(f'coreTeam2 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": coreTeam2})}')
    print(f'person_1 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_1})}')
    print(f'person_2 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_2})}')
    print(f'person_3 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_3})}')
    print(f'person_4 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_4})}')
    print(f'person_5 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_5})}')
    print(f'person_6 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_6})}')
    print(f'person_7 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_7})}')

    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_1}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_2}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_3}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_4}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_5}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_6}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_7}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_8}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_9}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_10}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_11}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_12}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_13}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_14}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_15}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_16}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_17}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_18}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_19}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_20}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_21}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_22}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_23}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_24}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_25}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_26}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_27}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_28}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_29}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_30}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_31}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_32}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_33}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_34}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_35}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_36}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_37}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_38}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_39}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_40}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_41}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_42}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_43}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_44}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_45}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_46}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_47}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_48}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_49}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_50}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_51}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_52}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_53}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_54}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_55}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_56}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_57}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_58}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_59}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_60}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_61}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_62}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_63}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_64}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_65}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_66}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_67}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_68}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_69}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_70}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_71}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_72}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_73}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_74}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_75}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_76}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_77}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_78}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_79}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_80}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_81}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_82}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_83}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_84}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_85}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_86}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_87}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_88}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_89}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_90}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_91}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_92}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_93}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_94}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_95}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_96}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_97}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_98}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_99}) == 0
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_100}) == 0





    amount_to_send = 1 * wbtc_decimals * .20

    print(f'money to approve : {amount_to_send}')


    total_to_deposit = amount_to_send
  
    mocked_wbtc.approve(TheRanchBullsMintAndReward,total_to_deposit, {"from":owner})
    fund_tx = TheRanchBullsMintAndReward.fundAndRewardBulls(1,20,total_to_deposit,{"from": owner})
    print(fund_tx.info())

    mocked_wbtc.approve(TheRanchBullsMintAndReward,total_to_deposit, {"from":owner})
    fund_tx = TheRanchBullsMintAndReward.fundAndRewardBulls(21,40,total_to_deposit,{"from": owner})
    print(fund_tx.info())


    mocked_wbtc.approve(TheRanchBullsMintAndReward,total_to_deposit, {"from":owner})
    fund_tx = TheRanchBullsMintAndReward.fundAndRewardBulls(41,60,total_to_deposit,{"from": owner})
    print(fund_tx.info())


    mocked_wbtc.approve(TheRanchBullsMintAndReward,total_to_deposit, {"from":owner})
    fund_tx = TheRanchBullsMintAndReward.fundAndRewardBulls(61,80,total_to_deposit,{"from": owner})
    print(fund_tx.info())


    mocked_wbtc.approve(TheRanchBullsMintAndReward,total_to_deposit, {"from":owner})
    fund_tx = TheRanchBullsMintAndReward.fundAndRewardBulls(81,100,total_to_deposit,{"from": owner})
    print(fund_tx.info())



    assert TheRanchBullsMintAndReward.monthlyRaffleBalance.call() == (1*10**8) * .05




    print(f'person_2: {TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_2})}')
    print(f'person_20: {TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_20})}')
    print(f'person_60: {TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_60})}')




    TheRanchBullsMintAndReward.setMonthlyMaintenanceFeePerNFT(14*10**6)   # 14 dollars in USDC.e for round 2
    assert TheRanchBullsMintAndReward.calculatedMonthlyMaintenanceFee.call() == 14*10**6


    tx_update_fees = TheRanchBullsMintAndReward.updateMaintenanceFeesForTheMonth()
    print(tx_update_fees.info())

    tx_updateMonthsBehind = TheRanchBullsMintAndReward.updateMonthsBehindMaintenanceFeeDueDate()
    print(tx_updateMonthsBehind)

    print("#######################################################################################")
    print(f'\t\t\t\t\t AFTER FUNDING AND UPDATING')
    print("#######################################################################################")
    print(f'coreTeam_1 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(coreTeam1)}')
    print(f'coreTeam_2 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(coreTeam2)}')
    print(f'person_1 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_1)}')
    print(f'person_2 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_2)}')
    print(f'person_3 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_3)}')
    print(f'person_4 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_4)}')
    print(f'person_5 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_5)}')
    print(f'person_6 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_6)}')
    print(f'person_7 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_7)}')

    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(coreTeam1) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(coreTeam2) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_1) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_2) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_3) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_4) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_5) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_6) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_7) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_8) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_9) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_10) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_11) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_12) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_13) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_14) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_15) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_16) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_17) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_18) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_19) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_20) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_21) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_22) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_23) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_24) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_25) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_26) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_27) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_28) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_29) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_30) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_31) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_32) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_33) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_34) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_35) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_36) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_37) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_38) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_39) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_40) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_41) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_42) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_43) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_44) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_45) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_46) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_47) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_48) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_49) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_50) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_51) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_52) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_53) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_54) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_55) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_56) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_57) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_58) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_59) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_60) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_61) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_62) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_63) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_64) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_65) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_66) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_67) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_68) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_69) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_70) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_71) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_72) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_73) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_74) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_75) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_76) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_77) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_78) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_79) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_80) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_81) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_82) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_83) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_84) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_85) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_86) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_87) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_88) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_89) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_90) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_91) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_92) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_93) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_94) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_95) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_96) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_97) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_98) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_99) == 14*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_100) == 14*10**6



    print('\n')
    

    print(f'coreTeam_1 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(coreTeam1)}')
    print(f'coreTeam_2 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(coreTeam2)}')
    print(f'person_1 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_1)}')
    print(f'person_2 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_2)}')
    print(f'person_3 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_3)}')
    print(f'person_4 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_4)}')
    print(f'person_5 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_5)}')
    print(f'person_6 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_6)}')
    print(f'person_7 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_7)}')



    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_1) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_2) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_3) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_4) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_5) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_6) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_7) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_8) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_9) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_10) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_11) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_12) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_13) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_14) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_15) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_16) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_17) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_18) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_19) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_20) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_21) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_22) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_23) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_24) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_25) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_26) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_27) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_28) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_29) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_30) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_31) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_32) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_33) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_34) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_35) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_36) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_37) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_38) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_39) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_40) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_41) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_42) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_43) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_44) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_45) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_46) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_47) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_48) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_49) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_50) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_51) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_52) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_53) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_54) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_55) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_56) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_57) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_58) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_59) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_60) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_61) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_62) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_63) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_64) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_65) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_66) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_67) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_68) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_69) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_70) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_71) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_72) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_73) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_74) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_75) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_76) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_77) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_78) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_79) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_80) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_81) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_82) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_83) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_84) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_85) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_86) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_87) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_88) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_89) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_90) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_91) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_92) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_93) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_94) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_95) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_96) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_97) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_98) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_99) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_100) == 1

    print('\n')

    print(f'liquidation list: {TheRanchBullsMintAndReward.getLiquidatedArray()}')

    print('\n')

    print(f'coreTeam1 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": coreTeam1})}')
    print(f'coreTeam2 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": coreTeam2})}')
    print(f'person_1 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_1})}')
    print(f'person_2 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_2})}')
    print(f'person_3 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_3})}')
    print(f'person_4 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_4})}')
    print(f'person_5 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_5})}')
    print(f'person_6 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_6})}')
    print(f'person_7 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_7})}')
    
    expected_wbtc_rewards = (((1*10**8) * 0.85) / 100) * 0.98
    assert mocked_wbtc.balanceOf(TheRanchBullsMintAndReward) == 1*10**8


    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_1}) == expected_wbtc_rewards
    print(f'expected WBTC rewards: {expected_wbtc_rewards}')
    print(f'Total Mints: {TheRanchBullsMintAndReward.totalSupply()}')

    
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_1}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_2}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_3}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_4}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_5}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_6}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_7}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_8}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_9}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_10}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_11}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_12}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_13}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_14}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_15}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_16}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_17}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_18}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_19}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_20}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_21}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_22}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_23}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_24}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_25}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_26}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_27}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_28}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_29}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_30}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_31}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_32}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_33}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_34}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_35}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_36}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_37}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_38}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_39}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_40}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_41}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_42}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_43}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_44}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_45}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_46}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_47}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_48}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_49}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_50}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_51}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_52}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_53}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_54}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_55}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_56}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_57}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_58}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_59}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_60}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_61}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_62}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_63}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_64}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_65}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_66}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_67}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_68}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_69}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_70}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_71}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_72}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_73}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_74}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_75}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_76}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_77}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_78}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_79}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_80}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_81}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_82}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_83}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_84}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_85}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_86}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_87}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_88}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_89}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_90}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_91}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_92}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_93}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_94}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_95}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_96}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_97}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_98}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_99}) == expected_wbtc_rewards
    assert TheRanchBullsMintAndReward.getWBTCRewardBalanceForAddress({"from": person_100}) == expected_wbtc_rewards


