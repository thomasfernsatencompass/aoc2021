inputs = `00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010`.split("\n").map(a => a.split("").map(x => x == '1'))

function part1(inputs) {
    let end = "";
    for (let i=0; i<inputs[0].length; i++) {
        let trues = inputs.filter(x => x[i] == true)
        let falses = inputs.filter(x => x[i] == false)

        if (trues.length >= falses.length) {
            end += "1";
        } else {
            end += "0";
        }
    } 
    
    let flipped = end.split("").map(x => x == '1' ? '0' : '1').join("")
    return parseInt(end, 2) * parseInt(flipped, 2)
}

const part1ans = part1(inputs)
console.log(`part 1: ${part1ans}`)

function part2(inputs, oxygen=true) {
    let result = inputs
    let index = 0;
    do {
        let trues = result.filter(x => x[index] == true)
        let falses = result.filter(x => x[index] == false)

        if (oxygen) {
            if (trues.length >= falses.length) {
                result = trues;
            } else {
                result = falses;
            }
        } else {
            if (falses.length > trues.length) {
                result = trues;
            } else {
                result = falses;
            }
        }

        index += 1;
    } while(result.length > 1)

    let binaryStr = result.pop().map(x => x ? 1 : 0).join("")
    return parseInt(binaryStr, 2)
}
 
const oxygen = part2(inputs, true)
const scrubber = part2(inputs, false)

const part2ans = oxygen * scrubber
console.log(`part 2: ${part2ans}`)
