using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace carrots
{
    class Program
    {
        static void Main(string[] args)
        {
            int cont = 0;
            int solved = 0;

            string[] input = Console.ReadLine().Split(' ');

            cont = Convert.ToInt32(input[0]);
            solved = Convert.ToInt32(input[1]);

            string[] descriptions = new string[cont];

            for (int i = 0; i < cont; i++)
            {
                descriptions[i] = Console.ReadLine();
            }

            Console.WriteLine(solved);
        }
    }
}