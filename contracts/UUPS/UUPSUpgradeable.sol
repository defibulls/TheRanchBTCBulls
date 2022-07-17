// // SPDX-License-Identifier: MIT
// // OpenZeppelin Contracts (last updated v4.5.0) (proxy/utils/UUPSUpgradeable.sol)

// pragma solidity ^0.8.0;


// import "@openzeppelin/contracts-upgradeable/interfaces/draft-IERC1822Upgradeable.sol";
// import "@openzeppelin/contracts-upgradeable/proxy/utils/Initializable.sol";
// import "@openzeppelin/contracts-upgradeable/proxy/ERC1967/ERC1967UpgradeUpgradeable.sol";



// // contract UUPSUpgradeable is Initializable, IERC1822ProxiableUpgradeable, ERC1967UpgradeUpgradeable  {
// //     /// @notice From Openzeppelin ERC1967Upgrade abstract contract
// //     constructor(address _logic) payable {
// //         _setImplementation(_logic);
// //     }

// //     /// Returns the implementation contract address
// //     /// @return address
// //     function _implementation() internal view virtual override returns (address) {
// //         return _getImplementation();
// //     }

// //     /// Storage slot with the address of the current implementation.
// //     /// This is the keccak-256 hash of "eip1967.proxy.implementation" subtracted by 1, and is
// //     /// validated in the constructor.
// //     /// @notice From Openzeppelin ERC1967Upgrade abstract contract
// //     /// @return bytes32
// //     function _getImplementationSlot() private view returns (bytes32){
// //         // Equivalent to:
// //         // bytes32(uint256(keccak256("eip1967.proxy.implementation")) - 1)
// //         return 0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc;
// //     }

// //     /// Returns the current implementation address.
// //     /// @notice From Openzeppelin ERC1967Upgrade abstract contract
// //     /// @return address
// //     function _getImplementation() private view returns (address) {
// //         return StorageSlot.getAddressSlot(_getImplementationSlot()).value;
// //     }

// //     /// Stores a new address in the EIP1967 implementation slot.
// //     /// @notice From Openzeppelin ERC1967Upgrade abstract contract
// //     function _setImplementation(address newImplementation) private {
// //         require(Address.isContract(newImplementation), "ERC1967: new implementation is not a contract");
// //         StorageSlot.getAddressSlot(_getImplementationSlot()).value = newImplementation;
// //     }
// // }




















// /**
//  * @dev An upgradeability mechanism designed for UUPS proxies. The functions included here can perform an upgrade of an
//  * {ERC1967Proxy}, when this contract is set as the implementation behind such a proxy.
//  *
//  * A security mechanism ensures that an upgrade does not turn off upgradeability accidentally, although this risk is
//  * reinstated if the upgrade retains upgradeability but removes the security mechanism, e.g. by replacing
//  * `UUPSUpgradeable` with a custom implementation of upgrades.
//  *
//  * The {_authorizeUpgrade} function must be overridden to include access restriction to the upgrade mechanism.
//  *
//  * _Available since v4.1._
//  */
// contract UUPSUpgradeable is Initializable, IERC1822ProxiableUpgradeable, ERC1967UpgradeUpgradeable {
//     function __UUPSUpgradeable_init() internal onlyInitializing {
//     }

//     function __UUPSUpgradeable_init_unchained() internal onlyInitializing {
//     }
//     /// @custom:oz-upgrades-unsafe-allow state-variable-immutable state-variable-assignment
//     address private immutable __self = address(this);

//     /**
//      * @dev Check that the execution is being performed through a delegatecall call and that the execution context is
//      * a proxy contract with an implementation (as defined in ERC1967) pointing to self. This should only be the case
//      * for UUPS and transparent proxies that are using the current contract as their implementation. Execution of a
//      * function through ERC1167 minimal proxies (clones) would not normally pass this test, but is not guaranteed to
//      * fail.
//      */
//     modifier onlyProxy() {
//         require(address(this) != __self, "Function must be called through delegatecall");
//         require(_getImplementation() == __self, "Function must be called through active proxy");
//         _;
//     }

//     /**
//      * @dev Check that the execution is not being performed through a delegate call. This allows a function to be
//      * callable on the implementing contract but not through proxies.
//      */
//     modifier notDelegated() {
//         require(address(this) == __self, "UUPSUpgradeable: must not be called through delegatecall");
//         _;
//     }

//     /**
//      * @dev Implementation of the ERC1822 {proxiableUUID} function. This returns the storage slot used by the
//      * implementation. It is used to validate that the this implementation remains valid after an upgrade.
//      *
//      * IMPORTANT: A proxy pointing at a proxiable contract should not be considered proxiable itself, because this risks
//      * bricking a proxy that upgrades to it, by delegating to itself until out of gas. Thus it is critical that this
//      * function revert if invoked through a proxy. This is guaranteed by the `notDelegated` modifier.
//      */
//     function proxiableUUID() external view virtual override notDelegated returns (bytes32) {
//         return _IMPLEMENTATION_SLOT;
//     }

//     /**
//      * @dev Upgrade the implementation of the proxy to `newImplementation`.
//      *
//      * Calls {_authorizeUpgrade}.
//      *
//      * Emits an {Upgraded} event.
//      */
//     function upgradeTo(address newImplementation) external virtual onlyProxy {
//         _authorizeUpgrade(newImplementation);
//         _upgradeToAndCallUUPS(newImplementation, new bytes(0), false);
//     }

//     /**
//      * @dev Upgrade the implementation of the proxy to `newImplementation`, and subsequently execute the function call
//      * encoded in `data`.
//      *
//      * Calls {_authorizeUpgrade}.
//      *
//      * Emits an {Upgraded} event.
//      */
//     function upgradeToAndCall(address newImplementation, bytes memory data) external payable virtual onlyProxy {
//         _authorizeUpgrade(newImplementation);
//         _upgradeToAndCallUUPS(newImplementation, data, true);
//     }

//     /**
//      * @dev Function that should revert when `msg.sender` is not authorized to upgrade the contract. Called by
//      * {upgradeTo} and {upgradeToAndCall}.
//      *
//      * Normally, this function will use an xref:access.adoc[access control] modifier such as {Ownable-onlyOwner}.
//      *
//      * ```solidity
//     function _authorizeUpgrade(address) internal override onlyOwner {}
//      * ```
//      */
//     function _authorizeUpgrade(address newImplementation) public virtual;

//     /**
//      * @dev This empty reserved space is put in place to allow future versions to add new
//      * variables without shifting down storage in the inheritance chain.
//      * See https://docs.openzeppelin.com/contracts/4.x/upgradeable#storage_gaps
//      */
//     uint256[50] private __gap;
// }
