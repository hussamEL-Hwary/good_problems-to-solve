//============================================================================
// Name        :
// Author      : hussam
// Version     :
// Copyright   :
// Description :
//============================================================================

#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n;
	scanf("%d", &n);
	if (n == 2)
	{
		cout << "NO\n";
		return 0;
	}
	if (n % 2 == 0)
		cout << "YES\n";
	else
	cout << "NO\n";

	return 0;
}