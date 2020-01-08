n=10
hoatchat=list()
for (i in 1:10) 
    hoatchat[[i]] = sample(LETTERS, sample(1:26, 1))

donthuoc = sample(LETTERS, 5)
ncbs = choose(length(donthuoc), 2)
cbs = combn(donthuoc, 2)

current_cbs = c()
for (i in 1:ncbs) current_cbs[i] = paste(sort(cbs[, i]), collapse='')
current_cbs

# sort(c('Z2345y', 'Dadsad', 'Cjkjk'))