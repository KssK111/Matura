# Napisz program sprawdzajacy, czy w tablicy n-elementowej znajduje sie liczba,
# ktora wystepuje wiecej niz n/4 razy. Przygotuj tablice tak,
# aby byla szansa wystapienia w niej takiej liczby.
# Przyjmij, ze n jest wielokrotnoscia 4.
# Program powinien wykonywac jak najmniej operacji.


const int N = 32;

void Losuj(int A[])
{
    int i, x = rand()%100;
    for(i = 0; i < N; i++)
    {
        if(rand()%4 != 0)
            A[i] = rand()%100;
        else
            A[i] = x;
    }
}

void Wypisz(int A[])
{
    int i;
    for(i = 0; i < N; i++)
    {
        cout << A[i] << " ";
    }
}

// szukanie elementu wystepujacego wiecej niz n/4 razy
int ZnajdzSlabegoLidera(int A[])
{
    int licznik[3] = {0, 0, 0};
    int kandydat[3] = {-1, -1, -1};
    int i, j;

    bool wsrodKandydatow;

    for(i = 0; i < N; i++)
    {
        wsrodKandydatow = false;

        for(j = 0; j < 3; j++)
        {
            if(kandydat[j] == A[i])
            {
                licznik[j]++;
                wsrodKandydatow = true;
            }
        }

        if(!wsrodKandydatow)
        {
            if(licznik[0] == 0)
            {
                kandydat[0] = A[i];
                licznik[0] = 1;
            }
            else if(licznik[1] == 0)
            {
                kandydat[1] = A[i];
                licznik[1] = 1;
            }
            else if(licznik[2] == 0)
            {
                kandydat[2] = A[i];
                licznik[2] = 1;
            }
            else
            {
                for(j = 0; j < 3; j++)
                    licznik[j]--;
            }
        }
    }

    for(j = 0; j < 3; j++)
    {
        int licznik = 0;
        for(i = 0; i < N; i++)
        {
            if(A[i] == kandydat[j])
                licznik++;
        }

        if(licznik > N/4)
            return kandydat[j];
    }

    return -1;
}

int main()
{
    srand(time(NULL));

    int A[N];

    Losuj(A);
    Wypisz(A);

    cout << endl;

    int lider = ZnajdzSlabegoLidera(A);
    if(lider != -1)
    {
        cout << "Slabym liderem (wiecej niz n/4 razy) jest " << lider;
    }
    else
    {
        cout << "Brak";
    }

    return 0;
}
