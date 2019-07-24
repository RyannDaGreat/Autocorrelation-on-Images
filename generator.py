folder='/Users/Ryan/Desktop/Autocorrelation on Images'
def testurl(url):
    imname=random_namespace_hash(3)
    im=load_image_from_url(url)
    save_image(im,folder+'/'+imname+'_0')
    out=rgbauto(im)
    save_image(out,folder+'/'+imname+'_1')
def rgbauto(pin):
    out= np.transpose([auto(pin[:,:,0]),auto(pin[:,:,1]),auto(pin[:,:,2])],(1,2,0))
    out=np.roll(out,out.shape[0]//2,0)
    out=np.roll(out,out.shape[1]//2,1)
    return out
def auto(im):
    #im=rgb_to_grayscale(im)
    return full_range(i(np.abs(f(im))**2).real)
i=np.fft.ifft2
f=np.fft.fft2
ans="""https://static.turbosquid.com/Preview/2014/08/01__17_25_29/cliff-texture-35x2.jpg3caf222c-56da-4d89-bbef-a99c9192da76Original.jpg
http://lh3.ggpht.com/_9lcs1G94AbE/SdTzrxhnAXI/AAAAAAAABcw/FrxiCwDjVOE/filterforge1_thumb%5B2%5D.jpg?imgmax=800
https://www.filterforge.com/filters/3131.jpg
https://dumielauxepices.net/sites/default/files/drawn-texture-sand-texture-580536-4221573.jpg
https://i.pinimg.com/236x/d2/6c/35/d26c356ab1544961b94b1b7cb9f8c109--volcanic-ash-photo-paint.jpg
http://musicments.com/img/d_default/metal-floor-texture/metal-floor-texture-filter-forge-5c73fe3d0c9be.jpg
https://skybase.files.wordpress.com/2012/01/woodtexturea1.jpg
https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRusIX9rFze0frlZnUw_WvfhSoc3DczBU7Si9ipnoYgrcrV7cVe
https://farm9.staticflickr.com/8391/8535899481_37930f066e_b.jpg
https://live.staticflickr.com/5624/23449221670_415418bdc1_z.jpg
http://s3.amazonaws.com/everystockphoto/fspid/16/05/04/84/filterforge-texture-stone-16050484-l.jpg
http://www.gamasutra.com/db_area/images/news2001/9466/texture.jpg"""
ans=ans.splitlines()
for _ in ans:
    try:
        testurl(_)
    except:pass
ans="""http://online-drawinglessons.com/wp-content/uploads/2016/12/how-to-draw-spongebob-step-by-step-1.jpg
https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcReJINSiUVH7I6gCLUnYgw6Bd3BlJZuNqwx-eQKAZoWG3Ivl29H
https://www.easy-drawings-and-sketches.com/images/cartoon-kitten23s.jpg
https://i.pinimg.com/originals/2c/f3/3f/2cf33f40b1d65d86ec4128aed8b7b123.jpg
https://www.drawingtutorials101.com/drawing-tutorials/For-Kids/Cartoons-for-Kids/funny-cartoon-egg/how-to-draw-Funny-Cartoon-Egg-step-0.png
https://i.pinimg.com/originals/1f/2c/6e/1f2c6e2f2677aa16f5e2f82cc45686dd.jpg
https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkv5CSjgrMEi09wID-iYD2929u9W4-WzFXSPgF2D4ct9U_O8C9
https://www.shareicon.net/data/2016/01/13/702711_toys_512x512.png
https://www.drawingnow.com/file/videos/image/how-to-draw-easy-cartoons.jpg
http://www.clker.com/cliparts/f/4/7/9/14297862011507722948kitty.png
http://www.how-to-draw-cartoons-online.com/image-files/how-to-draw-hello-kitty.gif"""
ans=ans.splitlines()
for _ in ans:
    try:
        testurl(_)
    except:pass
def testurl(url):
    imname=random_namespace_hash(3)
    im=load_image_from_url(url)
    save_image(im,folder+'/'+imname+'_0')
    out=rgbauto(im)
    save_image(out,folder+'/'+imname+'_1')
ans=rgbauto(load_image_from_url(ans[2]))
display_image(ans)
ans="""http://online-drawinglessons.com/wp-content/uploads/2016/12/how-to-draw-spongebob-step-by-step-1.jpg
https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcReJINSiUVH7I6gCLUnYgw6Bd3BlJZuNqwx-eQKAZoWG3Ivl29H
https://www.easy-drawings-and-sketches.com/images/cartoon-kitten23s.jpg
https://i.pinimg.com/originals/2c/f3/3f/2cf33f40b1d65d86ec4128aed8b7b123.jpg
https://www.drawingtutorials101.com/drawing-tutorials/For-Kids/Cartoons-for-Kids/funny-cartoon-egg/how-to-draw-Funny-Cartoon-Egg-step-0.png
https://i.pinimg.com/originals/1f/2c/6e/1f2c6e2f2677aa16f5e2f82cc45686dd.jpg
https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkv5CSjgrMEi09wID-iYD2929u9W4-WzFXSPgF2D4ct9U_O8C9
https://www.shareicon.net/data/2016/01/13/702711_toys_512x512.png
https://www.drawingnow.com/file/videos/image/how-to-draw-easy-cartoons.jpg
http://www.clker.com/cliparts/f/4/7/9/14297862011507722948kitty.png
http://www.how-to-draw-cartoons-online.com/image-files/how-to-draw-hello-kitty.gif"""
ans=ans.splitlines()
for _ in ans:
    try:
        testurl(_)
    except Exception as e:
        print_stack_trace(e)
        
