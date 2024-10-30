import java.util.*;

public class pick {
    public static void main(String[] args) {
        Set<String> peoples = new HashSet<>(Arrays.asList(
                "강지민", "강현호", "권남희", "김민철", "김홍범", "김지원", "박주찬",
                "신희원", "윤재은", "윤희준", "이국건", "임남기"
        ));

        Set<String> done = new HashSet<>(Arrays.asList(

                ));

        List<String> rest = new ArrayList<>(peoples);
        rest.removeAll(done);

        System.out.println(rest);

        Random random = new Random();
        String randomStudent = rest.get(random.nextInt(rest.size()));
        System.out.println(randomStudent);
    }
}
