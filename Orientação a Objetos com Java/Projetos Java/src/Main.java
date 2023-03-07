
public class Main {

	
	public static void main(String[] args) {
		String palavra = "Banana";
		char letraQueDesejoSubstituir = 'n';
		char letraSubstituta = '+';
		char novaLetra;
		String novaPalavra = "";
		for (int i=0;i<palavra.length();i++) {
			char letraAtual = palavra.charAt(i);
			if(letraAtual == letraQueDesejoSubstituir) {
				novaLetra = letraSubstituta;
			}
			else {
				novaLetra = letraAtual;
			}
			novaPalavra = novaPalavra+novaLetra;
		}
		System.out.println(novaPalavra);

	}

}
