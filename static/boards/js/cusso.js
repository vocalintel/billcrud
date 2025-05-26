const enab = document.getElementById("enable")
const prod = document.getElementById("product")
const pla = document.getElementById("plans")
const acco = document.getElementById("account")
const elev = document.getElementById("eleven")
const twel = document.getElementById("twelve")
const thir = document.getElementById("thirten")
const four = document.getElementById("fourten")
enab.onclick = function (){
if(elev.style.display !== "none"){
	elev.style.display = "block";
	enab.style.color = "black";
	enab.style.backgroundColor= "white";
	prod.style.color = "white";
	prod.style.backgroundColor= "royalblue";
	pla.style.color = "white";
	pla.style.backgroundColor= "royalblue";
	acco.style.color = "white";
	acco.style.backgroundColor= "royalblue";
	twel.style.display = "none";
	thir.style.display = "none";
	four.style.display = "none";
}else{
	elev.style.display = "block";
	enab.style.color = "black";
	enab.style.backgroundColor= "white";
	prod.style.color = "white";
	prod.style.backgroundColor= "royalblue";
	pla.style.color = "white";
	pla.style.backgroundColor= "royalblue";
	acco.style.color = "white";
	acco.style.backgroundColor= "royalblue";
	twel.style.display = "none";
	thir.style.display = "none";
	four.style.display = "none";
	}
};
prod.onclick = function (){
if(twel.style.display !== "none"){
	twel.style.display = "block";
	prod.style.color = "black";
	prod.style.backgroundColor= "white";
	enab.style.color = "white";
	enab.style.backgroundColor= "royalblue";
	pla.style.color = "white";
	pla.style.backgroundColor= "royalblue";
	acco.style.color = "white";
	acco.style.backgroundColor= "royalblue";
	elev.style.display = "none";
	thir.style.display = "none";
	four.style.display = "none";
}else{
	twel.style.display = "block";
	prod.style.color = "black";
	prod.style.backgroundColor= "white";
	enab.style.color = "white";
	enab.style.backgroundColor= "royalblue";
	pla.style.color = "white";
	pla.style.backgroundColor= "royalblue";
	acco.style.color = "white";
	acco.style.backgroundColor= "royalblue";
	elev.style.display = "none";
	thir.style.display = "none";
	four.style.display = "none";
	}
};
pla.onclick = function (){
if(thir.style.display !== "none"){
	thir.style.display = "block";
	pla.style.color = "black";
	pla.style.backgroundColor= "white";
	prod.style.color = "white";
	prod.style.backgroundColor= "royalblue";
	enab.style.color = "white";
	enab.style.backgroundColor= "royalblue";
	acco.style.color = "white";
	acco.style.backgroundColor= "royalblue";
	twel.style.display = "none";
	elev.style.display = "none";
	four.style.display = "none";
}else{
	thir.style.display = "block";
	pla.style.color = "black";
	pla.style.backgroundColor= "white";
	prod.style.color = "white";
	prod.style.backgroundColor= "royalblue";
	enab.style.color = "white";
	enab.style.backgroundColor= "royalblue";
	acco.style.color = "white";
	acco.style.backgroundColor= "royalblue";
	twel.style.display = "none";
	elev.style.display = "none";
	four.style.display = "none";
	}
};
acco.onclick = function (){
if(four.style.display !== "none"){
	four.style.display = "block";
	acco.style.color = "black";
	acco.style.backgroundColor= "white";
	prod.style.color = "white";
	prod.style.backgroundColor= "royalblue";
	enab.style.color = "white";
	enab.style.backgroundColor= "royalblue";
	pla.style.color = "white";
	pla.style.backgroundColor= "royalblue";
	twel.style.display = "none";
	elev.style.display = "none";
	thir.style.display = "none";
}else{
	four.style.display = "block";
	acco.style.color = "black";
	acco.style.backgroundColor= "white";
	prod.style.color = "white";
	prod.style.backgroundColor= "royalblue";
	enab.style.color = "white";
	enab.style.backgroundColor= "royalblue";
	pla.style.color = "white";
	pla.style.backgroundColor= "royalblue";
	twel.style.display = "none";
	elev.style.display = "none";
	thir.style.display = "none";
	}
};
