// Instructions
// Write a JavaScript program that recreates the pattern below.
// Do this challenge twice: first by using one loop, then by using two nested for loops (Nested means one inside the other - check out this tutorial of nested loops).
// Do this Daily Challenge by youself, without looking at the answers on the internet.
// *  
// * *  
// * * *  
// * * * *  
// * * * * *
// * * * * * *
 const starCycle = 6;
// let stars = "";
// for (let i =0; i < starCycle;i++){
//     stars = stars + "*";
//     console.log(stars);
// }
for (let i = 0;i < starCycle;i++) {
    const numberOfStars = i + 1;
    let starLine = "";
    for (let j  = 0; j < numberOfStars; j++) {
        starLine = starLine + "*";
    }
    console.log(starLine);
}
