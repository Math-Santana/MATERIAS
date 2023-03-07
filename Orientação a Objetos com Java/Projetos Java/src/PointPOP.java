
public class PointPOP {
	
	public static void setX(PointCoord pc,int x) {
		pc.x = x;
	}
	
	public static void setY(PointCoord pc, int y) {
		pc.y = y;
	}

	public static void getX(PointCoord pc) {
		return pc.x;
	}
	
	public static void getY(PointCoord pc) {
		return pc.y;
	}
	
	public static void main(String[] args) {
		setX(new PointCoord(),10);

	}

}


class PointCoord{
	int x;
	int y;
	
}
