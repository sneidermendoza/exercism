using System;

static class AssemblyLine
{
    public static double SuccessRate(int speed)
    {
        double rate = 0;
        if (speed == 0)
        {
            rate = 0;
        }
        else if (speed >= 1 && speed <= 4)
        {
            rate = 1;
        }
        else if (speed >= 5 && speed <= 8)
        {
            rate = 0.9;
        }
        else if (speed == 9)
        {
            rate = 0.8;
        }
        else if (speed == 10)
        {
            rate = 0.77;
        }
        return rate;
    }

    public static double ProductionRatePerHour(int speed)
    {
        double production = 0;
        double successRate = SuccessRate(speed);
        
        return production = (speed * 221) * successRate;
    }

    public static int WorkingItemsPerMinute(int speed)
    {
        int car_minutes = 0;
        double production_rate_per_hour = ProductionRatePerHour(speed);

        return car_minutes = (int)(production_rate_per_hour/60);
    }
}
