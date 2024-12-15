// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

contract Register { // Declares a new contract named Register
    string private info; 
    /* declares a private state variable info of type string.
    Being private, this variable can only be accessed and modified within this contract.*/

    constructor() {
        info = "python script reads blocked value successfully.";
    }

    function getInfo() public view returns  (string memory) {
        return info;
        /*
        public: Anyone can call this function.
        view: The function does not modify the state of the contract.
        returns (string memory): The function returns a string stored in memory.
        */
    }

    function setInfo (string memory _info) public {
        info = _info;
        /*
        public: Anyone can call this function.
        string memory _info: The function takes one parameter _info of type string, stored in memory.
        */
    }

}