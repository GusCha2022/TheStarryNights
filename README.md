
This is my project of admission into Makers Fellowship - to create an NFT collection and deploy it on polygon network

This project was based on the Brazilian flag - It's stars inside the blue circle represent each a state and have those positions following the stars position on the 15 of november, 1889, the day of proclamation of republic.

To create the images, I looked into nasa and yale stars catalog, but couldn't find a great source. Therefore I started to look into free Skymap generators and after a long search found https://www.fourmilab.ch/cgi-bin/Yoursky, which has a footnote that reads "Images produced by Your Sky are in the public domain and may be used in any manner without permission, restriction, attribution, or compensation. Back links to Your Sky are welcome."

As I only had 5 days to work with, I decided not to think too much and use webscraping to generate and save images for different cities at diferent dates. I recognize there may be smarter ways to achieve this, maybe to somehow download the engine or webscrape asynchronously. Researching about NFTs, I found around 10,000 tokens would be a good number, so I settled to use the whole year of 2022 and different influential and important cities spread around the world, to produce more unique skymaps. "scraper.py" is tge script to generate images

Cities chosen are ["New York", "Boston", "Madrid", "Washington DC", "San Francisco", "London", "Toronto", "Dublin", "Mexico City", "Chicago", "Los Angeles", "Paris", "Vienna", "Stockholm", "Zurich", "Helsinki", "Kyiv", "Cairo", "Tel Aviv", "Beijing", "Shanghai", "Seoul", "Singapore", "Tokyo", "Hong Kong", "Moscow", "Sydney", "Cape Town", "Rio de Janeiro"]

For the blockchain, it was required to deploy it on Polygon mainnet, so I based myself a lot in this article: https://medium.com/pinata/how-to-create-layer-2-nfts-with-polygon-and-ipfs-aef998ff8ef2. Firstly, I uploaded all the images to IPFS and then, with the CID address I generated the metadata with "metadatagen.py" and also uploaded it to the pinata service, and therefore IPFS.

Then, always following the article, I copied "NFT.sol" from it, installed hardhat and changed "hardhat.config.js" to use the Mumbai Polygon testnet, get my metamask keys to an .env, deployed the contract and minted a single token, through "mint-script.js". Later on, it was only needed to change the network to the mainnet and repeat the whole process. 

These function may be changed and updated as I want to take the project further, with the first thing being a script to batch mint tokens, as my last attempt to do it didn't work 100%.

Contract address: 0xbD789294B5beE658cC0ab938ff8FD92f97C5F247
