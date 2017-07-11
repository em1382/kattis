using System;

namespace Pot
{
    public class Program
    {
        static void Main(string[] args)
        {
            string number = String.Empty;
            int addends = int.Parse(Console.ReadLine());
            int x = 0;

            for (int i = 0; i < addends; i++)
            {
                number = Console.ReadLine();

                double n = double.Parse(number.Substring(0, number.Length - 1));
                double p = double.Parse(number.Substring(number.Length - 1));

                x += Convert.ToInt32(Math.Pow(n, p).ToString());
            }

            Console.WriteLine(x);
        }
    }
}