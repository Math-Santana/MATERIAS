
public class NovoReplace {

	public static void main(String[] args) {
		NovoReplace.replace("Matheus", 'a', 'b');

	}
	
	public static String replace(String s, char target, char replacement) {

	    char ListadeCaracteres [] = s.toCharArray();
	    System.out.println(ListadeCaracteres);

	    for (int i = 0; i < ListadeCaracteres.length; i++) {

	        if (ListadeCaracteres[i] == target) {

	        	ListadeCaracteres[i] = replacement;

	        }

	    }

	    String sfinal = "";

	    for (int i = 0; i < ListadeCaracteres.length; i++) {

	        sfinal = sfinal + ListadeCaracteres[i];

	    }

	    return sfinal;

	    }

}
