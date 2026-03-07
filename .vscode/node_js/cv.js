class BankAccount{
    constructor(name){
        this._name = name;
        this._balance = 0;
    }
    get name(){
        return this._name;
    }
    set name(name){
        this._name = name;
    }
    deposit(amount){
        this._balance += amount;
        return this._balance;
    }
    withdraw(amount){
        this._balance -= amount;
		return balance;
    }
    showInfo(){
        console.log("Name: ", this._name);
        console.log("Balance: ", this._balance);
    }
}
class CurrentAccount extends BankAccount{
    constructor(name){
        super(name);
    }
    transfer(account, amount) {
			this._balance -= amount;
			account._balance += amount;
    } //transfer Saving account
}
class SavingAccount extends BankAccount{
     constructor(name, balance = 0, interestRate = 0.05) {
        super(name);
        this._balance = balance;
        this._interestRate = interestRate;
    }
    transfer(account, amount) {
			this._balance -= amount;
			account._balance += amount;
	}//tranfer current account
    showInfo() {
			console.log("Name: ", this._name);
			console.log("Balance: ", this._balance);
			console.log("interestRate: ", this._interestRate);
		}
}
const sa  = new SavingAccount("Loc", 1000000, 0.07);
const sa1 = new SavingAccount("Dung", 0, 0.05);

const ca  = new CurrentAccount("Loc");
const ca1 = new CurrentAccount("Dung");
ca._balance += 100000;          // thêm tiền vào current account
ca.transfer(ca1, 30000);        // Loc → Dung 30k
sa.transfer(ca, 500000);        // Saving → Current 500k
ca1.transfer(sa1, 20000);       // Current → Saving 20k

ca.showInfo();
ca1.showInfo();
sa.showInfo();
sa1.showInfo();
