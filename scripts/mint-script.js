const hre = require("hardhat");
async function main() {
const NFT = await hre.ethers.getContractFactory("Starry");
const URI = "ipfs://QmeQ7oggTWD8jSfjWN6xMbe3zj12EAZNPvKdCYEFxRxpdL/10499.json" 
const WALLET_ADDRESS = "0xebdF6DBB69c7ebba53E56D878283464a8e5a491f"
const CONTRACT_ADDRESS = "0xbD789294B5beE658cC0ab938ff8FD92f97C5F247"
const contract = NFT.attach(CONTRACT_ADDRESS);
await contract.mint(WALLET_ADDRESS, URI);
console.log("NFT minted:", contract);
}
main().then(() => process.exit(0)).catch(error => {
console.error(error);
process.exit(1);
});
