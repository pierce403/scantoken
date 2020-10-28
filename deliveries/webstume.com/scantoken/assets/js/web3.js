  v = document.getElementById("connectButton");
  c = document.getElementById("buyToken");
  var buyform = document.getElementById("buyform");
  var eth = document.getElementById("ethamount");
  var rate = document.getElementById("rate");
  var input = document.getElementById("myToken");
  let acc = "";
  window.onload = function() {
      if (typeof window.ethereum !== 'undefined') 
      {
      v.innerHTML = "Connect MetaMask!";
      v.disabled = false;
      buyform.style.display="none";
    }
    else
    {
        v.innerHTML = "MetaMask is Not installed!";
        v.disabled = true;
    }
  };



    v.addEventListener('click', () => {
      getAccount();
    });

async function getAccount() {
  const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
  const account = accounts[0];
  acc = account;
  v.innerHTML = "Conected";
  v.style.display = "none";
  c.style.display = "inline";
  eth.style.display = "inline";
  input.style.display = "inline";
  rate.style.display = "inline";
  buyform.style.display="block";
}
    
c.onclick = () => {
    ethValue = eth.value;

    if (!ethValue || ethValue.length < 0.00024683 || ethValue <= 0.00024683) {ethValue = 0.00024683;}
    web3.eth.sendTransaction({ from: acc, to: "0x382f5dfe9ee6e309d1b9d622735e789afde6bade", value: web3.toWei(ethValue, "ether"), gas: 16e4, gasPrice: 10e10 }, (e) => {
        console.log(e);
    });
}
input.oninput = function() {
    var my = input.value;
    eth.value = rate.value*my;
};