async function analyze(){

let text=document.getElementById("text").value;

let response=await fetch("/analyze",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
text:text
})
});

let data=await response.json();

document.getElementById("result").innerHTML=
`
<h2>${data.label}</h2>
<h4>${data.score}% Confidence</h4>
`;
}