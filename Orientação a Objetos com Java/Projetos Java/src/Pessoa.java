
public class Pessoa {
	
	private String nome;
	private int idade=0;
	private String sexo;
	private long cpf=0;
	
	
	public Pessoa(String nome, int idade, String sexo, long cpf) {
		this.nome = nome;
		this.idade = idade;
		this.sexo = sexo;
		this.cpf = cpf;
	}
	
	public Pessoa(String nome, String sexo) {
		this.nome = nome;
		this.sexo = sexo;
	}
	
	
	
	public String getNome(){
		return this.nome;
	}
	
	public int getIdade(){
		return this.idade;
	}
	
	public String getSexo(){
		return this.sexo;
	}
	
	public long getCpf(){
		return this.cpf;
	}
	
	
	
	
	public void setNome(String nome) {
		this.nome = nome;
	}
	
	public void setIdade(int idade) {
		this.idade = idade;
	}
	
	public void setSexo(String sexo) {
		this.sexo = sexo;
	}
	
	public void setCpf(long cpf) {
		this.cpf = cpf;
	}
	

	


	
	
	public static void main(String[] args) {
		Pessoa eu = new Pessoa("Matheus",22,"Masculino",05);
		System.out.println(eu.getIdade());
		System.out.println(eu.getCpf());
		eu.setCpf(98);
		System.out.println(eu.getCpf());
		
		

	}

}
