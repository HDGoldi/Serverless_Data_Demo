{
    "sensorId": {{random.number(50)}},
    "currentTemperature": {{random.number(
        {
            "min":10,
            "max":150
        }
    )}},
    "status": "{{random.weightedArrayElement(
       {
        "weights": [0.64,0.02,0.34],
        "data": ["OK","FAIL","WARN"]
}
    )}}"
}
