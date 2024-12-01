#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define da_append(xs, x)\
    do {\
    if (xs.count >= xs.capacity) {\
        if (xs.capacity == 0) xs.capacity = 256;\
        else xs.capacity *= 2;\
        xs.items = realloc(xs.items, xs.capacity * sizeof(*xs.items));\
    }\
    xs.items[xs.count++] = x;\
    } while(0);\

typedef struct {
    int *items;
    int count;
    int capacity;
} Locations;

int parse_file(char *path, Locations *left, Locations *right)
{
    FILE *f = fopen(path, "r");
    if (f == NULL) {
        perror("Error opening file");
        return EXIT_FAILURE;
    }

    int left_loc, right_loc;
    while (fscanf(f, "%d %d", &left_loc, &right_loc) == 2) {
        da_append((*left), left_loc); 
        da_append((*right), right_loc);
    }

    fclose(f);
    return EXIT_SUCCESS;
}

int partition(Locations *locs, int low, int high)
{
    int pivot = locs->items[high];
    int index = low;

    for (int j = low; j < high; j++) {
        if (locs->items[j] <= pivot) {
            if (j != index) {
                locs->items[index] = locs->items[index] ^ locs->items[j];
                locs->items[j] = locs->items[index] ^ locs->items[j];
                locs->items[index] = locs->items[index] ^ locs->items[j];
            }

            index++;
        }
    }

    if (high != index) {
        locs->items[index] = locs->items[index] ^ locs->items[high];
        locs->items[high] = locs->items[index] ^ locs->items[high];
        locs->items[index] = locs->items[index] ^ locs->items[high];
    }

    return index;
}

void quicksort(Locations *locs, int low, int high)
{
    if (low < high) {
        int pivot_index = partition(locs, low, high);
        quicksort(locs, low, pivot_index - 1);
        quicksort(locs, pivot_index + 1, high);
    }
}

void sort(Locations *locs)
{
    if (locs->count > 1) {
        quicksort(locs, 0, locs->count - 1);
    }
}

int main()
{
    Locations left = {0};
    Locations right = {0};

    parse_file("input.txt", &left, &right);

    // part 1
    {
        int sum = 0;
        sort(&left);
        sort(&right);

        for (int i = 0; i < left.count; i++) {
            sum += abs(left.items[i] - right.items[i]);
        }

        printf("sum of distances: %d\n", sum);
    }

    // part 2
    {
        int sum = 0;
        for (int i = 0; i < left.count; i++) {
            int current = 0;
            for (int j = 0; j < right.count; j++) {
                if (right.items[j] == left.items[i]) {
                    current++;
                }
            }
            sum += left.items[i] * current;
        }

        printf("sum of appearances: %d\n", sum);
    }
    free(left.items);
    free(right.items);

    return 0;
}