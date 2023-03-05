"""
hint 1
Try to find indexes of next smaller and previous smaller for every element.
Next smaller is the nearest smallest element on right side of arr[i].
Similarly, previous smaller element is the nearest smallest element on left side of arr[i].
If there is no smaller element on right side, then next smaller is n.
If there is no smaller on left side, then previous smaller is -1.

hint2
if you have indexes of next and previous smaller, arr[i] is a minimum of a window of length “right[i] – left[i] – 1”.
After this you will get an array whose each entry will be the lengths of windows for which the elements are minimum.
Eg: {7, 3, 2, 1, 7, 1, 2}, in this array, first element is minimum in window of size 7, second element is minimum in window of size 3, and so on.

Now create an auxiliary array ans[n+1] to store the result.
Values in ans[] can be filled by iterating through right[] and left[]

 for (int i=0; i < n; i++) {
        // length of the interval
        int len = right[i] - left[i] - 1;
        // a[i] is the possible answer for this length len interval
        ans[len] = max(ans[len], arr[i]);
    }
Note that ans[0] or answer for length 0 is useless.
Result for length i, i.e. ans[i] would always be greater or same as result for length i+1, i.e., ans[i+1].

hint 3

Some entries in ans[] are 0 and yet to be filled.
Few important observations to fill remaining entries
a) Result for length i, i.e. ans[i] would always be greater or same as result for length i+1, i.e., ans[i+1].
b) If ans[i] is not filled it means there is no direct element which is minimum of length i and therefore either the element of length ans[i+1], or ans[i+2], and so on is same as ans[i]
So we fill rest of the entries using loop.

    for (int i=n-1; i>=1; i--)
        ans[i] = max(ans[i], ans[i+1]);


"""

