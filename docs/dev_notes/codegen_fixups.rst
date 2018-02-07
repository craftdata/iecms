After the fixups you need to manually do the following
1). CsiView (Change this - it does not exist)
2). Change the T_Casecategorychecklist views to
            views = [CasecategoryView, CasechecklistView, ]

3). Finally for wtf_PageForm
enable the exlude to
exclude = ['page_image']
