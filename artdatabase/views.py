from django.shortcuts import render
from .models import Art, Artist
from django.shortcuts import render, get_object_or_404
from .forms import ArtForm, ArtistForm
from django.shortcuts import redirect

def search(request):
    if request.method == "POST":
        search_artist_by_name = request.POST.get('search-artist-by-name');
        search_artist_by_id = request.POST.get('search-artist-by-id');
        search_art_by_artist_id = request.POST.get('search-art-by-artist-id');

        if search_artist_by_name is not None and search_artist_by_name != '':
            return redirect('artist_list', artist_name=search_artist_by_name)
        elif search_artist_by_id is not None and search_artist_by_id != '':
            return redirect('artist_detail', pk=search_artist_by_id)
        elif search_art_by_artist_id is not None and search_art_by_artist_id != '':
            return redirect('art_list', artist_id=search_art_by_artist_id)
            
    return render(request, 'artdatabase/search.html', {'search': search})

def art_list(request, artist_id=None):
    if artist_id is not None:
        arts = Art.objects.filter(artist=artist_id)
    else:
        arts = Art.objects.all()
    return render(request, 'artdatabase/art_list.html', {'arts': arts})

def art_detail(request, pk):
    art = get_object_or_404(Art, pk=pk)
    return render(request, 'artdatabase/art_detail.html', {'art': art})

def art_new(request):
    if request.method == "POST":
        form = ArtForm(request.POST)
        if form.is_valid():
            art = form.save(commit=False)
            art.save()
            return redirect('art_detail', pk=art.pk)
    else:
        form = ArtForm()
    return render(request, 'artdatabase/art_edit.html', {'form': form})

def art_edit(request, pk):
    art = get_object_or_404(Art, pk=pk)
    if request.method == "POST":
        form = ArtForm(request.POST, instance=art)
        if form.is_valid():
            art = form.save(commit=False)
            art.save()
            return redirect('art_detail', pk=art.pk)
    else:
        form = ArtForm(instance=art)
    return render(request, 'artdatabase/art_edit.html', {'form': form})

def artist_list(request, artist_name=None):
    if artist_name is not None:
        artists = Artist.objects.filter(name__icontains=artist_name)
    else:
        artists = Artist.objects.all()
    return render(request, 'artdatabase/artist_list.html', {'artists': artists})

def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'artdatabase/artist_detail.html', {'artist': artist})

def artist_new(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save(commit=False)
            artist.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm()
    return render(request, 'artdatabase/artist_edit.html', {'form': form})

def artist_edit(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    if request.method == "POST":
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist = form.save(commit=False)
            artist.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'artdatabase/artist_edit.html', {'form': form})
