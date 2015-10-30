using System;

// Two 'Person' collect stones in a 'Quarry'
// when 10 stones collected --> change stones for money

namespace InTheQuarry
{
    public class MainClass
    {

        public static void Main(string[] args)
        {
            
            Quarry quarry1 = new Quarry();
            Person person1 = new Person("Mike");
            StoneDealer stoneDealer1 = new StoneDealer("MyStoneDealer");

            for (int i = 0; i < 1000; i++)
            {
                System.Threading.Thread.Sleep(500); // implement later into the work-method
                person1.Work(quarry1, person1);
                person1.SellWorkedStones(person1, stoneDealer1);

                Console.WriteLine("{0} stones in the quarry.", quarry1.Stone);
            }
            
            Console.Read();
        }
    }

    public class Quarry
    {
        private int stone;
        public int Stone { get; set; }
        
        public Quarry()
        {
            Stone = 10000;
        }

        public void WorkInQuarry(Quarry q, QuarryWorker[] workers)  // method
        {
            throw new NotImplementedException();
        }
        
    }

    public abstract class QuarryWorker
    {
        //public abstract void Work(Quarry quarry);
    }

    public class Machine : QuarryWorker
    {
        public void Work(Quarry quarry)
        {
            throw new NotImplementedException();
        }
    }

    public class Person : QuarryWorker
    {
        private string name;
        public string Name { get; set; }

        private int workedStone;
        public int WorkedStone { get; set; }

        private int money;
        public int Money { get; set; }

        public Person(string n)
        {
            WorkedStone = 0;
            Money = 0;
            Name = n;                
            Console.WriteLine("New Person created!");
        }

        public void Work(Quarry quarry, Person person)
        {
            WorkedStone += 1;
            quarry.Stone -= 1;
        }

        public void SellWorkedStones(Person person, StoneDealer stoneDealer)
        {
            if (person.WorkedStone >= 10)
            {
                Console.WriteLine("{0} wants to sell his workedStone", person.Name);
                StoneDealer.ChangeStonesToMoney(person, stoneDealer);
            }
        }
    }

    public class StoneDealer
    {
        private string name;
        public string Name { get; set; }

        private int workedStone;
        public int WorkedStone { get; set; }

        private int money;
        public int Money { get; set; }

        public StoneDealer(string n)
        {
            WorkedStone = 0;
            Money = 3000;
            Name = n;
        }

        // static - because I don't need an instance here
        public static void ChangeStonesToMoney(Person person, StoneDealer stoneDealer)
        {
            Console.WriteLine("{0} comes to the {1}.", person.Name, stoneDealer.Name);
            person.WorkedStone -= 10;
            stoneDealer.WorkedStone += 10;
            person.Money += 1;
            stoneDealer.Money -= 1;

            Console.WriteLine("{0} has now {1} dollar.", person.Name, person.Money);
        }
    }
}
