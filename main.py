huskylens2.I2CInit()
huskylens2.switchAlgorithm(huskylens2.Algorithm.AlgorithmSelfLearningClassification)
loops.everyInterval(500, function () {
    rekabit.setServoPosition(ServoChannel.S2, 50)
    rekabit.setServoPosition(ServoChannel.S1, 90)
    rekabit.setServoPosition(ServoChannel.S3, 0)
})
basic.forever(function () {
    for (let index = 0; index < 4; index++) {
    	
    }
})
