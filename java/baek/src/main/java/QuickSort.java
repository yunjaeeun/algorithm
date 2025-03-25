public class QuickSort {
    public static void main(String[] args) {
        int[] arr = {4, 3, 10, 2, 1, 9, 8, 6, 5};

        System.out.println("정렬 전");
        for (int i : arr) {
            System.out.print(i + " ");
        }
        System.out.println();

        quickSort(arr, 0, arr.length - 1);

        System.out.println("정렬 후");
        for (int i : arr) {
            System.out.print(i + " ");
        }
    }

    public static void quickSort(int[] arr ,int low, int high) {
        if (low < high) {
            int pivotIdx = partition(arr, low, high);   // 피벗 위치 찾기
            quickSort(arr, low, pivotIdx - 1);     // 피벗보다 작은 부분 정렬
            quickSort(arr, pivotIdx + 1, high);    // 피벗보다 큰 부분 정렬
        }
    }

    public static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];  // 마지막 원소를 피벗으로 선택
        int i = low - 1;        // 피벗보다 작은 원소의 끝 인덱스

        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                // arr[i]와 arr[j] 위치 교환
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        // 피벗 위치 이동
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;

        // 피벗 위치 반환
        return i + 1;
    }
}
