using System;

namespace Bijele
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] original = new int[] { 1, 1, 2, 2, 2, 8 };
            string[] pieces = Console.ReadLine().Split(' ');
            string missing = string.Empty;

            for (int i = 0; i < pieces.Length; i++)
            {
                missing += original[i] - int.Parse(pieces[i]) + " ";
            }

            Console.WriteLine(missing.Trim());
        }
    }
}