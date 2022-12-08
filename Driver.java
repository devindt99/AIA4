import java.util.List;
import java.io.BufferedReader;  
import java.io.FileReader;  
import java.io.IOException; 

public class Driver {
	
	String line = "";  	
	String splitBy = ",";  

	try   
	{  
	//parsing a CSV file into BufferedReader class constructor  
	BufferedReader br = new BufferedReader(new FileReader("bank.csv"));  
	while ((line = br.readLine()) != null)   //returns a Boolean value  
	{  
	String[] employee = line.split(splitBy);    // use comma as separator  
	System.out.println("Employee [First Name=" + employee[0] + ", Last Name=" + employee[1] + ", Designation=" + employee[2] + ", Contact=" + employee[3] + ", Salary= " + employee[4] + ", City= " + employee[5] +"]");  
	}  
	}   
	catch (IOException e)   
	{  
	e.printStackTrace();  
	}  

	static double [][] X= {
			{0,0},
			{1,0},
			{0,1},
			{1,1}
	};
	static double [][] Y= {
			{0},{1},{1},{0}
	};

	public static void main(String[] args) {
		
		NeuralNetwork nn = new NeuralNetwork(2,10,1);
		
		
		List<Double>output;
		
		nn.fit(X, Y, 50000);
		double [][] input = {
				{0,0},{0,1},{1,0},{1,1}	
		};
		for(double d[]:input)
		{
			output = nn.predict(d);
			System.out.println(output.toString());
		}		

	}

}