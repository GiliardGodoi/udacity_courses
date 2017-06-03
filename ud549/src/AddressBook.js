

function AddressBook(){
    this.lsContact = [];
    this.initialComplete = false;
}

AddressBook.prototype.getInitialContacts = function(callback){
    var self = this;
    
    setTimeout( function(){
        self.initialComplete = true;
        if(callback){
            callback();
        }
    }, 3);
}

AddressBook.prototype.addContact = function addcontact(contact){
        this.lsContact.push(contact)
    }
AddressBook.prototype.getContact = function getcontact(index){
        return this.lsContact[index];
    }

AddressBook.prototype.deleteContact = function(index) {
    this.lsContact.splice(index,1);
}