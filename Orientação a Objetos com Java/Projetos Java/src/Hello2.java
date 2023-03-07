
public class Hello2 {

	public static void main(String[] args) {
		System.out.println("Hello2!!");
		
		//Classe String com objeto s, e dentro desse objeto é "Java"
		String s  = "Java";
		
		//Printando o objeto
		System.out.println(s);
		
		//Chama um método charAt para o objeto s, e retorna uma letra de acordo
		//com a posicao desejada, 0 no caso é o primeiro elemento, portanto
		//o resultado é J, que é a primeira letra de Java
		System.out.println(s.charAt(0));
		
		//Comando for em que i varia de 0 até o tamanho do string que está no 
		//objeto s, acrescentado 1 em i a cada iteração. Dentro do for, será
		//impresso cada caracter da string
		for (int i=0;i<=s.length();i++) {
			System.out.println(s.charAt(i));
		}
		

	}

}
