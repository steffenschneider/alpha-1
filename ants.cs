using System;
using System.Collections.Generic;
					
public static class Program
{
    public static void Main()
    {
        var random = new Random();

        var iterations = 1000000;

        var numberOfAnts = 10;
        var ants = CreateAntCollection(numberOfAnts);

        var numberOfFoods = 2;
        var foods = CreateFoodCollection(numberOfFoods);

        for (var iteration = 0; iteration < iterations; iteration++)
        {
            foreach (var ant in ants)
            {
                var x = (random.Next(3) - 1) + ant.Position.X;
                var y = (random.Next(3) - 1) + ant.Position.Y;

                ant.Move(x, y);
            }

            for (var i = ants.Count - 1; i >= 0; i--)
            {
                var ant = ants[i];

                for (var y = foods.Count - 1; y >= 0; y--)
                {
                    var food = foods[y];

                    if (ant.CanReach(food))
                    {
                        Console.WriteLine(
                            "{0} {1} {2} found food at {3}",
                            iteration,
                            ant,
                            ant.Position,
                            food.Position);

                        ant.Eat(food);

                        foods.RemoveAt(y);
                    }
                }
            }

            RedrawScreen();
        }
    }

    private static List<Ant> CreateAntCollection(int count)
    {
        var ants = new List<Ant>(count);

        for (var i = 0; i < count; i++)
        {
            var name = string.Format("ant-{0}", i);

            var ant = new Ant(name);

            ants.Add(ant);
        }

        return ants;
    }

    private static List<Food> CreateFoodCollection(int count)
    {
        var foods = new List<Food>(count);

        for (var i = 0; i < count; i++)
        {
            foods.Add(new Food());
        }

        foods[0].Move(110, 100);
        foods[1].Move(120, 100);

        return foods;
    }
	
	private static void RedrawScreen()
	{
		// TODO: Redraw the screen!
	}
}

class Ant
{
    public Ant(string name)
    {
        Name = name;
        Position = new Position(0, 0);
    }

    public string Name { get; private set; }

    public int FoodEaten { get; private set; }

    public Position Position { get; private set; }

    public void Eat(Food food)
    {
        FoodEaten += 1;
    }

    public bool CanReach(Food food)
    {
        var distance = Position.DistanceTo(food.Position);

        return distance < 3.0;
    }

    public void Move(int x, int y)
    {
        Position = new Position(x, y);
    }

    public override string ToString()
    {
        return Name;
    }
}

class Food
{
    public Food()
    {
        Position = new Position(0, 0);
    }

    public Position Position { get; private set; }

    public void Move(int x, int y)
    {
        Position = new Position(x, y);
    }
}

struct Position
{
	public readonly int X;

    public readonly int Y;
	
    public Position(int x, int y)
    {
        X = x;
        Y = y;
    }

    public double DistanceTo(Position other)
    {
        var x = X - other.X;
        var y = Y - other.Y;

        var distance = Math.Sqrt(Math.Pow(x, 2) + Math.Pow(y, 2));

        return distance;
    }

    public override string ToString()
    {
        return string.Format("{0},{1}", X, Y);
    }
}
