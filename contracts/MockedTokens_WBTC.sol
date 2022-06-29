// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";


contract MockedTokens_WBTC is ERC20 {
    // wei
    constructor(uint256 initialSupply) ERC20("Wrapped_BTC", "WBTC") {
        _mint(msg.sender, initialSupply);
    }

    function decimals() public view virtual override returns (uint8) {
    return 8;
    }

}


