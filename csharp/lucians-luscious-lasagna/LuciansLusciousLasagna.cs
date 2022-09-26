class Lasagna
{
    // TODO: define the 'ExpectedMinutesInOven()' method

    // TODO: define the 'RemainingMinutesInOven()' method

    // TODO: define the 'PreparationTimeInMinutes()' method

    // TODO: define the 'ElapsedTimeInMinutes()' method

    private readonly int EXPETED_OVEN_TIMES = 40;
    private readonly int Minutes = 2;
    
    public int ExpectedMinutesInOven()
    {
        return EXPETED_OVEN_TIMES;
    }


    public int RemainingMinutesInOven(int timeInTheOven)
    {
        return EXPETED_OVEN_TIMES - timeInTheOven ;
    }


    public int PreparationTimeInMinutes(int layers)
    {
        return layers * Minutes;
    }


    public int ElapsedTimeInMinutes(int LayersPerMinute, int minutesInTheOven )
    {
        return PreparationTimeInMinutes(LayersPerMinute) + minutesInTheOven;
    }
}
