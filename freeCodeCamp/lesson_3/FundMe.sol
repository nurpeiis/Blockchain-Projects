//SPDX-License-Identifier: MIT

pragma solidity >=0.8.0 <0.9.0;

//https://github.com/smartcontractkit/chainlink/blob/develop/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";



contract FundMe {
    
    mapping(address => uint256) public addressToAmountFunded;
    address[] public funders;
    //constructor needed to define owner
    
    address public owner;
    
    constructor () public{
        owner = msg.sender;
    }
    //functioin is used to pay
    function fund() public payable{
        uint256 minUsd = 50 * 10 **18;
        require(getConversionRate(msg.value) >=  minUsd, "More eth needed");
        addressToAmountFunded[payable(msg.sender)] += msg.value;    
        funders.push(msg.sender); 
    }
    
    function getVersion() public view returns (uint256){
        //get rinkeby eth/usd priceFeed
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        return priceFeed.version();
    }
    
    function getPrice() public view returns (uint256){
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        (,int256 answer,,,) = priceFeed.latestRoundData();
        return uint256(answer * 10**10);
    }
    
    function  getConversionRate(uint256 ethAmount) public view returns (uint256){
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUsd = (ethPrice * ethAmount)/10**18;
        
        return ethAmountInUsd;
    }
    
    modifier  onlyOwner{
        require(msg.sender == owner);
        _;
    }
    function withdraw() payable onlyOwner public{
        payable(msg.sender).transfer(address(this).balance);
        for (uint256  fIndx = 0; fIndx  < funders.length; fIndx++){
            address funder = funders[fIndx];
            addressToAmountFunded[funder] = 0;
        }
        funders = new address[](0);
    }
}