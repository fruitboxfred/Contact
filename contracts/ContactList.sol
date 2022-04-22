// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract ContactList {
     struct Contact {
        // assosiate name with phone number
        string name;
        string phoneNumber;
    
    }
    Contact[] public contact; //array for list of contacts
    mapping(string => string) public nameToPhoneNumber; //used to map name to phone number, so you can get phone number using name
    function addContact(string memory _name, string memory _phoneNumber) public {
        contact.push(Contact(_name, _phoneNumber)); //append to  Contact[] array
        nameToPhoneNumber[_name] = _phoneNumber; //use name to get phone number
    }
}

