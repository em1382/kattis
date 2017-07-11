using System;

namespace DetailedDifferences
{
    class Program
    {
        static void Main(string[] args)
        {
            int cases = int.Parse(Console.ReadLine());
            string str1, str2, diff;

            for (int i = 0; i < cases; i++)
            {
                str1 = Console.ReadLine();
                str2 = Console.ReadLine();
                diff = string.Empty;

                for (int j = 0; j < str1.Length; j++)
                {
                    if (!str1[j].Equals(str2[j]))
                    {
                        diff += "*";
                    }
                    else
                    {
                        diff += ".";
                    }
                }

                Console.WriteLine(str1);
                Console.WriteLine(str2);
                Console.WriteLine(diff);
                Console.WriteLine();
            }
        }
    }
}