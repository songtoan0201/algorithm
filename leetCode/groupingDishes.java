class Dishes {
    public static String[][] groupingDishes(String[][] dishes) {
        Map<String, ArrayList<String>> map = new HashMap<String, ArrayList<String>>();
        for (int i = 0; i < dishes.length; i++) {
            for (int j = 1; j < dishes[i].length; j++) {
                if (map.containsKey(dishes[i][j])) {
                    map.get(dishes[i][j]).add(dishes[i][0]);
                } else {
                    map.put(dishes[i][j], new ArrayList<String>());
                    map.get(dishes[i][j]).add(dishes[i][0]);
                }
            }
        }

        ArrayList<String[]> groupDishes = new ArrayList<String[]>();
        for (String ingredient : map.keySet()) {
            if (map.get(ingredient).size() >= 2) {
                ArrayList<String> a1 = new ArrayList<String>();
                a1.add(ingredient);
                ArrayList<String> foods = map.get(ingredient);
                Collections.sort(foods);
                a1.addAll(foods);
                String[] arr = new String[a1.size()];
                groupDishes.add(a1.toArray(arr));
            }
        }

        Collections.sort(groupDishes, (a, b) -> a[0].compareTo(b[0]));

        // String[][] arr = new String[groupDishes.size()][];
        // arr = groupDishes.toArray(arr);

        System.out.print(map);
        return groupDishes.toArray(new String[0][]);
    }

    public static void main(String[] args) {
        String[][] dishes = { { "Salad", "Tomato", "Cucumber", "Salad", "Sauce" },
                { "Pizza", "Tomato", "Sausage", "Sauce", "Dough" }, { "Quesadilla", "Chicken", "Cheese", "Sauce" },
                { "Sandwich", "Salad", "Bread", "Tomato", "Cheese" } };

        System.out.print(groupingDishes(dishes));
    }
}
