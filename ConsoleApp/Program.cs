using System;

namespace ConsoleApp
{
    class Program
    {
        static void main(string[] args)
        {
            Console.WriteLine("Enter your score (0 - 100): ");
            double score = Convert.ToDouble(Console.ReadLine());
            if (score < 0 || score > 100)
            {
                Console.WriteLine("Invalid score. Please enter a value between 0 and 100.");
            }
            string grade;
            if (score >= 90)
            {
                grade = "A";
            }
            else if (score >= 80)
            {
                grade = "B";
            }
            else if (score >= 70)
            {
                grade = "C";
            }
            else if (score >= 60)
            {
                grade = "D";
            }
            else
            {
                grade = "F";
            }
            Console.WriteLine($"Your grade is: {grade}");
        }
    }
}
