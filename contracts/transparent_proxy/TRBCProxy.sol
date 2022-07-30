




### FILE NO LONGER BEING USED AS WHEN IN USE, IMAGES WOULD NOT SHOW UP ON OPENSEA ###






















// SPDX-License-Identifier: MIT

pragma solidity 0.8.7;

import "@openzeppelin/proxy/ERC1967/ERC1967Proxy.sol";
import "@openzeppelin/access/AccessControlEnumerable.sol";




/**
 * @dev This contract implements a proxy that is upgradeable by an admin.
 *
 * To avoid https://medium.com/nomic-labs-blog/malicious-backdoors-in-ethereum-proxies-62629adf3357[proxy selector
 * clashing], which can potentially be used in an attack, this contract uses the
 * https://blog.openzeppelin.com/the-transparent-proxy-pattern/[transparent proxy pattern]. This pattern implies two
 * things that go hand in hand:
 *

 * These properties mean that the DEFAULT_ADMIN_ROLE account can only be used for admin actions like upgrading the proxy.
 */
contract TRBCProxy is ERC1967Proxy, AccessControlEnumerable {

    /**
     * @dev Initializes an upgradeable proxy by the implementation at `_logic`, and
     * optionally initialized with `_data` as explained in {ERC1967Proxy-constructor}.
     */
    constructor(address _logic, bytes memory _data) payable ERC1967Proxy(_logic, _data) {

        // to grant and revoke any roles
        _setupRole(DEFAULT_ADMIN_ROLE, msg.sender);
    }


    /**
     * @dev Returns the current implementation.
     *
     *
     */
    function implementation() external returns (address implementation_) {
        implementation_ = _implementation();
    }

    /**
     * @dev Upgrade the implementation of the proxy.
     *
     * NOTE: Only the DEFAULT_ADMIN_ROLE can call this function.
     */
    function upgradeTo(address newImplementation) external  onlyRole(DEFAULT_ADMIN_ROLE) {
        _upgradeToAndCall(newImplementation, bytes(""), false);
    }

    /**
     * @dev Upgrade the implementation of the proxy, and then call a function from the new implementation as specified
     * by `data`, which should be an encoded function call. This is useful to initialize new storage variables in the
     * proxied contract.
     *
     * NOTE: Only the DEFAULT_ADMIN_ROLE can call this function. 
     */
    function upgradeToAndCall(address newImplementation, bytes calldata data) external payable  onlyRole(DEFAULT_ADMIN_ROLE) {
        _upgradeToAndCall(newImplementation, data, true);
    }
}
