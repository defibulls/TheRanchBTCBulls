// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MockedTokens_DAI is ERC20 {
    // wei
    constructor(uint256 initialSupply) ERC20("DAI Coin", "DAI") {
        _mint(msg.sender, initialSupply);
    }
}