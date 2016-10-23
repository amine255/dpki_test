

### Loading libraries:
require(data.table)

### Loadin data:
df_conso <- fread("df_conso.csv")
df_dju <- fread("df_dju.csv")

### Reformatting data, adding useful temporary columns:
DT <- df_conso[, bat := unlist(lapply(strsplit(df_conso$id_bat, split = "B"), function(x) return(paste0("B",x[2]))))]
DT[, id_site := unlist(lapply(strsplit(df_conso$id_bat, split = "B"), function(x) return(x[1])))]
DT[, id_bat := NULL]
DT[, dates_y_m := unlist(lapply(strsplit(df_conso$date, split = "-"), function(x) return(paste0(x[1], "-", x[2]))))]
setcolorder(DT, c("id_site", "date", "bat", "conso", "dates_y_m"))

### Joining the two dataframes:
setkey(DT, dates_y_m)
setkey(df_dju, month)
DT1 <- DT[df_dju, nomatch=0]
DT1[,dates_y_m:=NULL]

### Casting data:
DT_final <- dcast.data.table(DT1, id_site + date + dju ~ bat, value.var = "conso")
setcolorder(DT_final, c(names(DT_final)[1:2], names(DT_final)[4:(length(DT_final))], "dju"))

### NAs to zero:
na_to_zero <- function(DT){ 
        for (j in seq_len(ncol(DT)))
                set(DT, which(is.na(DT[[j]])), j, 0)
}

na_to_zero(DT_final)
